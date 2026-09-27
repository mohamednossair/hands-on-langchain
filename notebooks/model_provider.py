"""Shared chat and embedding model configuration for the book's notebooks."""

import os

from dotenv import find_dotenv, load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
import ollama


load_dotenv(find_dotenv(usecwd=True))

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "groq").strip().lower()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", os.getenv("MODEL", "qwen2.5:7b"))
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
MODEL = OLLAMA_MODEL if MODEL_PROVIDER == "ollama" else GROQ_MODEL
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")


def get_chat_model(temperature: float = 0.0):
    """Create the configured chat model."""
    if MODEL_PROVIDER == "groq":
        return ChatGroq(model=MODEL, temperature=temperature)
    if MODEL_PROVIDER != "ollama":
        raise ValueError("MODEL_PROVIDER must be 'ollama' or 'groq'.")

    options = {"model": MODEL, "temperature": temperature}
    if OLLAMA_BASE_URL:
        options["base_url"] = OLLAMA_BASE_URL
    return ChatOllama(**options)


def get_raw_chat_completion(
    messages: list[dict[str, str]],
    temperature: float = 0.0,
    max_completion_tokens: int | None = None,
    model: str | None = None,
) -> str:
    """Call the selected provider's native chat API."""
    model = model or MODEL
    if MODEL_PROVIDER == "groq":
        options = {"model": model, "messages": messages, "temperature": temperature}
        if max_completion_tokens is not None:
            options["max_completion_tokens"] = max_completion_tokens
        response = Groq().chat.completions.create(**options)
        return response.choices[0].message.content or ""
    if MODEL_PROVIDER != "ollama":
        raise ValueError("MODEL_PROVIDER must be 'ollama' or 'groq'.")

    options = {"temperature": temperature}
    if max_completion_tokens is not None:
        options["num_predict"] = max_completion_tokens
    client = ollama.Client(host=OLLAMA_BASE_URL or "http://localhost:11434")
    response = client.chat(model=model, messages=messages, options=options)
    return response.message.content


def get_embeddings():
    """Create the configured embeddings model (used by all providers)."""
    # Use sentence-transformers for local CPU-friendly embeddings
    # Note: This requires scipy to be properly installed
    try:
        from sentence_transformers import SentenceTransformer
        model_name = "sentence-transformers/all-mpnet-base-v2"
        model = SentenceTransformer(model_name)
        
        class LocalEmbeddings:
            def __init__(self, model):
                self.model = model
                self.dimension = model.get_embedding_dimension()
            
            def embed_documents(self, texts):
                return self.model.encode(texts, normalize_embeddings=True, batch_size=32).tolist()
            
            def embed_query(self, text):
                return self.model.encode(text, normalize_embeddings=True).tolist()
        
        return LocalEmbeddings(model)
    except ImportError as e:
        print(f"Warning: Could not load sentence-transformers: {e}")
        print("Falling back to Ollama embeddings if available")
        # Fallback to Ollama if sentence-transformers fails
        from langchain_ollama import OllamaEmbeddings
        options = {"model": "nomic-embed-text"}
        if OLLAMA_BASE_URL:
            options["base_url"] = OLLAMA_BASE_URL
        return OllamaEmbeddings(**options)