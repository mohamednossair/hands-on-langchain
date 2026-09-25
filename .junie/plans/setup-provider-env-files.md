---
sessionId: session-260925-180403-vynr
---

# Requirements

### Overview & Goals
Provide a separate, safe-to-commit environment template for Groq and Ollama so the user can choose a provider without editing a combined settings file.

### Scope
- Replace the current combined `.env.example` with `.env.ollama.example` and add `.env.groq.example`.
- Document copying the selected template to `.env`; keep `.env` as the only active file loaded by notebooks.
- Keep real API keys out of tracked templates; Groq users add their own `GROQ_API_KEY` in the ignored `.env`.
- Preserve shared Ollama embedding settings and existing optional integration settings.
- Do not change model selection logic or notebook behavior.

# Technical Design

### Current Implementation
- `notebooks/model_provider.py` calls `load_dotenv(find_dotenv(usecwd=True))`, so configuration is loaded from `.env` rather than provider-specific filenames.
- The helper already selects chat via `MODEL_PROVIDER`, uses `GROQ_API_KEY` for Groq, and keeps embeddings on Ollama.
- `README.md` currently instructs users to copy `.env.example` to `.env`; `.gitignore` excludes `.env`.

### Proposed Changes
- Make `.env.ollama.example` the default Ollama template with `MODEL_PROVIDER=ollama`, Ollama chat/model settings, and shared embedding configuration.
- Add `.env.groq.example` with `MODEL_PROVIDER=groq`, Groq model and a clearly commented `GROQ_API_KEY` placeholder, plus the shared Ollama embedding configuration.
- Retain the current optional integration settings in the templates so existing notebook setup remains available.
- Update `README.md` with explicit copy instructions for either provider and explain that switching providers means copying the other template over `.env`.
- Leave `notebooks/model_provider.py`, `.gitignore`, and provider APIs unchanged; templates remain trackable while the working `.env` remains ignored.

# Testing

### Validation Approach
- Confirm both templates specify the intended `MODEL_PROVIDER` and required provider-specific settings without containing a real API secret.
- Confirm the README commands target the existing `.env` loading convention and mention that Ollama embeddings are still needed with Groq chat.
- Run the existing provider unit tests in `tests/test_model_provider.py` to ensure the unchanged Groq/Ollama selection behavior remains valid.

# Delivery Steps

### ✓ Step 1: Add provider-specific environment templates
The repository contains distinct Ollama and Groq configuration examples that can safely be copied into the active `.env`.
- Rename the current combined `.env.example` to `.env.ollama.example` and retain its shared embedding and optional integration settings.
- Add `.env.groq.example` with Groq chat selection, model configuration, and a non-secret `GROQ_API_KEY` placeholder.
- Include the Ollama embedding settings in both templates because embeddings remain local when Groq is selected.

### ✓ Step 2: Document provider selection and validate setup
README setup instructions show how to activate either provider using the existing `.env` loader, and the provider behavior remains covered by tests.
- Update `README.md` setup instructions with the copy command for `.env.ollama.example` and the alternative for `.env.groq.example`.
- Explain that switching provider means replacing `.env`, where to put the Groq key, and that Ollama is still required for embeddings.
- Check that both template values and README instructions are consistent, then run `tests/test_model_provider.py`.