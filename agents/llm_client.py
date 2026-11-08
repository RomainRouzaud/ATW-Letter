"""
LLM Client abstraction layer.
Supports multiple providers: Mistral AI, Gemini, Ollama, IBM WatsonX (BAM).
Provider and config are loaded from config/llm_config.yaml.
"""
import os
import yaml
import json
import time
import requests
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "llm_config.yaml")


def load_llm_config() -> dict:
    """Load LLM configuration from YAML file."""
    if not os.path.exists(CONFIG_PATH):
        # Default to Mistral if no config exists yet
        return {"provider": "mistral", "model": "mistral-small-latest"}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class LLMClient:
    """
    Unified LLM client supporting:
      - mistral  : Mistral AI via REST API (needs MISTRAL_API_KEY in .env)
      - gemini   : Google Gemini via google-genai SDK
      - ollama   : Local Ollama (gemma, llama, mistral, etc.)
      - watsonx  : IBM WatsonX / BAM via REST API
    """

    def __init__(self):
        self.config = load_llm_config()
        self.provider = self.config.get("provider", "mistral")
        self.model = self.config.get("model", "mistral-small-latest")

    def generate(self, prompt: str, json_mode: bool = False) -> str | None:
        """
        Generate a response from the configured LLM.
        Returns the text response, or None on error.
        """
        if self.provider == "mistral":
            return self._generate_mistral(prompt, json_mode)
        elif self.provider == "gemini":
            return self._generate_gemini(prompt, json_mode)
        elif self.provider == "ollama":
            return self._generate_ollama(prompt, json_mode)
        elif self.provider == "watsonx":
            return self._generate_watsonx(prompt, json_mode)
        else:
            print(f"[LLM] Provider inconnu: {self.provider}")
            return None

    # ------------------------------------------------------------------
    # Mistral AI
    # ------------------------------------------------------------------
    def _generate_mistral(self, prompt: str, json_mode: bool) -> str | None:
        try:
            api_key = os.environ.get("MISTRAL_API_KEY") or self.config.get("api_key")
            if not api_key:
                print("[Mistral] MISTRAL_API_KEY manquante dans .env ou llm_config.yaml.")
                return None

            base_url = self.config.get("base_url", "https://api.mistral.ai/v1/chat/completions")
            model_name = self.model or "mistral-small-latest"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }

            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
            }
            if json_mode:
                payload["response_format"] = {"type": "json_object"}

            candidate_models = [model_name, "mistral-small-latest", "mistral-large-latest"]
            seen_models = set()
            ordered_models = []
            for m in candidate_models:
                if m not in seen_models:
                    seen_models.add(m)
                    ordered_models.append(m)

            for target_model in ordered_models:
                payload["model"] = target_model
                for attempt in range(3):
                    try:
                        resp = requests.post(base_url, json=payload, headers=headers, timeout=90)
                        if resp.status_code == 200:
                            data = resp.json()
                            choices = data.get("choices", [])
                            if choices:
                                return choices[0].get("message", {}).get("content", "")
                            return ""
                        elif resp.status_code in (429, 500, 503):
                            wait_sec = (attempt + 1) * 3
                            print(f"[Mistral] Statut {resp.status_code} sur {target_model} (tentative {attempt+1}/3), attente de {wait_sec}s...")
                            time.sleep(wait_sec)
                            continue
                        else:
                            print(f"[Mistral] Erreur HTTP {resp.status_code} sur {target_model}: {resp.text}")
                            break
                    except Exception as e:
                        print(f"[Mistral] Erreur requête sur {target_model}: {e}")
                        time.sleep(2)

            print("[Mistral] Impossible de générer la réponse après plusieurs tentatives.")
            return None
        except Exception as e:
            print(f"[Mistral] Erreur: {e}")
            return None

    # ------------------------------------------------------------------
    # Gemini (Google)
    # ------------------------------------------------------------------
    def _generate_gemini(self, prompt: str, json_mode: bool) -> str | None:
        try:
            from google import genai
            from google.genai import types

            api_key = os.environ.get("GEMINI_API_KEY") or self.config.get("api_key")
            if not api_key:
                print("[Gemini] GEMINI_API_KEY manquante.")
                return None

            # Gemini API requires the full 'models/' prefix
            model_name = self.model
            if not model_name.startswith("models/"):
                model_name = f"models/{model_name}"

            client = genai.Client(api_key=api_key)
            kwargs = {}
            if json_mode:
                kwargs["config"] = types.GenerateContentConfig(
                    response_mime_type="application/json"
                )

            # Retry loop with backoff and fallback models on 503 / 429
            candidate_models = [model_name, "models/gemini-flash-lite-latest", "models/gemini-3.1-flash-lite"]
            # Deduplicate while preserving order
            seen_models = set()
            ordered_models = []
            for m in candidate_models:
                if m not in seen_models:
                    seen_models.add(m)
                    ordered_models.append(m)

            for target_model in ordered_models:
                for attempt in range(3):
                    try:
                        response = client.models.generate_content(
                            model=target_model,
                            contents=prompt,
                            **kwargs
                        )
                        return response.text
                    except Exception as e:
                        err_str = str(e)
                        if any(w in err_str for w in ["503", "UNAVAILABLE", "RESOURCE_EXHAUSTED", "429"]):
                            wait_sec = (attempt + 1) * 3
                            print(f"[Gemini] Charge élevée sur {target_model} (tentative {attempt+1}/3), attente de {wait_sec}s...")
                            time.sleep(wait_sec)
                            continue
                        else:
                            print(f"[Gemini] Erreur sur {target_model}: {e}")
                            break

            print("[Gemini] Impossible de générer la réponse après tentatives et fallbacks.")
            return None
        except Exception as e:
            print(f"[Gemini] Erreur: {e}")
            return None

    # ------------------------------------------------------------------
    # Ollama (local)
    # ------------------------------------------------------------------
    def _generate_ollama(self, prompt: str, json_mode: bool) -> str | None:
        try:
            base_url = self.config.get("base_url", "http://localhost:11434")
            url = f"{base_url}/api/generate"
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            }
            if json_mode:
                payload["format"] = "json"

            resp = requests.post(url, json=payload, timeout=120)
            resp.raise_for_status()
            return resp.json().get("response", "")
        except Exception as e:
            print(f"[Ollama] Erreur: {e}")
            return None

    # ------------------------------------------------------------------
    # IBM WatsonX / BAM
    # ------------------------------------------------------------------
    def _generate_watsonx(self, prompt: str, json_mode: bool) -> str | None:
        try:
            api_key = os.environ.get("WATSONX_API_KEY") or self.config.get("api_key")
            project_id = os.environ.get("WATSONX_PROJECT_ID") or self.config.get("project_id")
            base_url = self.config.get(
                "base_url",
                "https://eu-de.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
            )

            if not api_key or not project_id:
                print("[WatsonX] WATSONX_API_KEY ou WATSONX_PROJECT_ID manquants.")
                return None

            # Obtain IAM bearer token
            iam_resp = requests.post(
                "https://iam.cloud.ibm.com/identity/token",
                data={
                    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                    "apikey": api_key,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=30
            )
            iam_resp.raise_for_status()
            bearer = iam_resp.json().get("access_token")

            payload = {
                "model_id": self.model,
                "input": prompt,
                "parameters": {
                    "max_new_tokens": 2048,
                    "temperature": 0.3,
                },
                "project_id": project_id,
            }

            resp = requests.post(
                base_url,
                json=payload,
                headers={
                    "Authorization": f"Bearer {bearer}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                timeout=120
            )
            resp.raise_for_status()
            results = resp.json().get("results", [])
            if results:
                return results[0].get("generated_text", "")
            return None
        except Exception as e:
            print(f"[WatsonX] Erreur: {e}")
            return None
