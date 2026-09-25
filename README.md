# Hands-On LangChain — Notebooks

Companion code for the book **[_Hands-On LangChain: Build LLM Applications and AI Agents with LangChain, LangGraph, LangMem, and LangSmith_](youssefhosni.gumroad.com/l/fowkx)** by **Youssef Hosni**.

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/0e7d1087-51f7-4ad8-81e5-0965bff9ec32"
    alt="Front cover"
    width="320"
  />
  &nbsp;&nbsp;
  <img
    src="https://github.com/user-attachments/assets/50ab8ebf-e4fa-4dad-8e58-5b4e59d3d5b5"
    alt="Back cover"
    width="320"
  />
</p>

Every chapter that contains code has a runnable Jupyter notebook here. The outputs shown in the book were produced by running these notebooks against **LangChain 1.x**.

## Setup

Install [Ollama](https://ollama.com/download), start its local service, and pull the embedding model. Pull the default Ollama chat model too if you want to use Ollama for chat:

```bash
ollama pull nomic-embed-text
ollama pull qwen2.5:7b
```

Then install the Python dependencies and configure the environment:

```bash
pip install --upgrade langchain langchain-ollama langchain-groq ollama groq langchain-community \
    langchain-text-splitters langgraph langmem langchain-classic \
    langsmith pydantic tiktoken chromadb faiss-cpu pypdf \
    ddgs docx2txt "unstructured[xlsx]" beautifulsoup4 python-dotenv jupyter -q

cp .env.ollama.example .env
```

The command above selects Ollama for chat. To use Groq instead, copy its template to `.env`:

```bash
cp .env.groq.example .env
```

The notebooks load configuration from `.env` only. To switch providers, copy the other template over `.env` (replacing the current configuration). Groq chat requires a `GROQ_API_KEY` from [console.groq.com/keys](https://console.groq.com/keys); add your key to `.env` only. `.env` is ignored by Git, so do not put a real key in either tracked template. The web-search examples use **DuckDuckGo**, which needs no key. The LangSmith chapters optionally use a `LANGSMITH_API_KEY` from [smith.langchain.com](https://smith.langchain.com).

Each template configures its provider's chat model and the shared Ollama embedding model. Ollama chat requires no API key. Ollama is still required for embeddings, so keep its service running and pull `nomic-embed-text` even when Groq is selected for chat. `MODEL=qwen2.5:7b` remains supported as a legacy alias for `OLLAMA_MODEL`. Set `OLLAMA_BASE_URL` if Ollama is not available at its default `http://localhost:11434`. If you change the embedding model, rebuild notebook-created vector stores because embedding dimensions may differ.

Then open any notebook and run it top to bottom.

## Notebooks

| Chapter | Notebook |
|---|---|
| 2 · Model I/O | `notebooks/02-model-io-prompts-and-parsing.ipynb` |
| 3 · Chains | `notebooks/03-chains.ipynb` |
| 4 · Memory | `notebooks/04-memory.ipynb` |
| 5 · Evaluation | `notebooks/05-evaluation.ipynb` |
| 6 · Document Loading | `notebooks/06-document-loading.ipynb` |
| 7 · Document Splitting | `notebooks/07-document-splitting.ipynb` |
| 8 · Vector Stores & Retrieval | `notebooks/08-vector-stores-and-retrieval.ipynb` |
| 9 · QA over Documents | `notebooks/09-question-answering-over-documents.ipynb` |
| 11 · Building Agents | `notebooks/11-building-agents.ipynb` |
| 12 · Agentic Web Search | `notebooks/12-agentic-web-search.ipynb` |
| 13 · Persistence & Streaming | `notebooks/13-persistence-and-streaming.ipynb` |
| 14 · Human-in-the-Loop | `notebooks/14-human-in-the-loop.ipynb` |
| 15 · Multi-Agent Essay Writer | `notebooks/15-multi-agent-essay-writer.ipynb` |
| 17 · Baseline Email Agent | `notebooks/17-baseline-email-agent.ipynb` |
| 18 · Semantic Memory | `notebooks/18-semantic-memory.ipynb` |
| 19 · Episodic Memory | `notebooks/19-episodic-memory.ipynb` |
| 20 · Procedural Memory | `notebooks/20-procedural-memory.ipynb` |
| 22 · Tracing with LangSmith | `notebooks/22-tracing-with-langsmith.ipynb` |
| 23 · Playground & Prompts Hub | `notebooks/23-playground-and-prompts-hub.ipynb` |

`notebooks/prompts.py` holds the shared prompt templates used by the LangMem chapters (17–20), and `notebooks/model_provider.py` holds the shared selectable chat-provider and Ollama embedding configuration. Sample data for the RAG and loader chapters is in `data/`.

*(Chapters 1, 10, 16, and 21 are conceptual and have no notebook.)*

## About the author

**Youssef Hosni** writes the *To Data & Beyond* newsletter — hands-on, practical guides on machine learning, LLMs, and generative AI. Find more at [todatabeyond.substack.com](https://todatabeyond.substack.com).
