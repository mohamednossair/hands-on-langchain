"""Shared chat and embedding model configuration for the book's notebooks."""

import os

from dotenv import find_dotenv, load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama, OllamaEmbeddings
import ollama


load_dotenv(find_dotenv(usecwd=True))

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "ollama").strip().lower()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", os.getenv("MODEL", "qwen2.5:7b"))
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
MODEL = OLLAMA_MODEL if MODEL_PROVIDER == "ollama" else GROQ_MODEL
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
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


def get_embeddings() -> OllamaEmbeddings:
    """Create the configured Ollama embeddings model (used by all providers)."""
    options = {"model": EMBEDDING_MODEL}
    if OLLAMA_BASE_URL:
        options["base_url"] = OLLAMA_BASE_URL
    return OllamaEmbeddings(**options)