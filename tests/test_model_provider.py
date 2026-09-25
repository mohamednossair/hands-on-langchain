import unittest
from unittest.mock import patch

from notebooks import model_provider


class ModelProviderTests(unittest.TestCase):
    def test_groq_chat_model_uses_selected_groq_model(self):
        with (
            patch.object(model_provider, "MODEL_PROVIDER", "groq"),
            patch.object(model_provider, "MODEL", "groq-test-model"),
            patch.object(model_provider, "ChatGroq") as chat_groq,
        ):
            model_provider.get_chat_model(temperature=0.2)

        chat_groq.assert_called_once_with(model="groq-test-model", temperature=0.2)

    def test_ollama_chat_model_remains_available(self):
        with (
            patch.object(model_provider, "MODEL_PROVIDER", "ollama"),
            patch.object(model_provider, "MODEL", "qwen-test-model"),
            patch.object(model_provider, "OLLAMA_BASE_URL", "http://ollama.test"),
            patch.object(model_provider, "ChatOllama") as chat_ollama,
        ):
            model_provider.get_chat_model(temperature=0.3)

        chat_ollama.assert_called_once_with(
            model="qwen-test-model",
            temperature=0.3,
            base_url="http://ollama.test",
        )

    def test_embeddings_stay_on_ollama_when_groq_chat_is_selected(self):
        with (
            patch.object(model_provider, "MODEL_PROVIDER", "groq"),
            patch.object(model_provider, "EMBEDDING_MODEL", "nomic-test-model"),
            patch.object(model_provider, "OllamaEmbeddings") as embeddings,
        ):
            model_provider.get_embeddings()

        embeddings.assert_called_once_with(model="nomic-test-model")

    def test_raw_groq_completion_uses_native_api(self):
        with (
            patch.object(model_provider, "Groq") as groq,
            patch.object(model_provider, "MODEL_PROVIDER", "groq"),
            patch.object(model_provider, "MODEL", "groq-test-model"),
        ):
            groq.return_value.chat.completions.create.return_value.choices[0].message.content = "answer"
            result = model_provider.get_raw_chat_completion(
                [{"role": "user", "content": "hello"}],
                temperature=0.4,
                max_completion_tokens=32,
            )

        self.assertEqual(result, "answer")
        groq.return_value.chat.completions.create.assert_called_once_with(
            model="groq-test-model",
            messages=[{"role": "user", "content": "hello"}],
            temperature=0.4,
            max_completion_tokens=32,
        )