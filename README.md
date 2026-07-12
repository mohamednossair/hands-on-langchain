# Hands-On LangChain — Notebooks

Companion code for the book **[_Hands-On LangChain: Build LLM Applications and AI Agents with LangChain, LangGraph, LangMem, and LangSmith_](youssefhosni.gumroad.com/l/fowkx)** by **Youssef Hosni**.

Every chapter that contains code has a runnable Jupyter notebook here. The outputs shown in the book were produced by running these notebooks against **LangChain 1.x**.

## Setup

```bash
# 1. Install dependencies
pip install --upgrade langchain langchain-openai langchain-community \
    langchain-text-splitters langgraph langmem langchain-classic \
    langsmith pydantic openai tiktoken chromadb faiss-cpu pypdf \
    ddgs docx2txt "unstructured[xlsx]" beautifulsoup4 python-dotenv jupyter -q

# 2. Configure your keys
cp .env.example .env      # then edit .env and add your OPENAI_API_KEY
```

At minimum you need `OPENAI_API_KEY`. The web-search examples (Part III) use **DuckDuckGo**, which needs no key. The LangSmith chapters (Part V) require a free `LANGSMITH_API_KEY` from [smith.langchain.com](https://smith.langchain.com).

The book uses a single chat model and embedding model, set in `.env`:

```
MODEL=gpt-5.4-mini
EMBEDDING_MODEL=text-embedding-3-small
```

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

`notebooks/prompts.py` holds the shared prompt templates used by the LangMem chapters (17–20). Sample data for the RAG and loader chapters is in `data/`.

*(Chapters 1, 10, 16, and 21 are conceptual and have no notebook.)*

## About the author

**Youssef Hosni** writes the *To Data & Beyond* newsletter — hands-on, practical guides on machine learning, LLMs, and generative AI. Find more at [todatabeyond.substack.com](https://todatabeyond.substack.com).
