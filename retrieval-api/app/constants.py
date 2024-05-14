from os import getenv

OPENROUTER_BASE = "https://openrouter.ai"
OPENROUTER_API_BASE = f"{OPENROUTER_BASE}/api/v1"
OPENROUTER_DEFAULT_CHAT_MODEL = "meta-llama/llama-3-70b-instruct:nitro"
# OPENROUTER_DEFAULT_CHAT_MODEL = getenv(
#    "OPENROUTER_DEFAULT_CHAT_MODEL", "meta-llama/llama-3-8b-instruct:free"
# )
OPENROUTER_API_KEY = getenv("OPENROUTER_API_KEY")
PROMPT_TEMPLATE = """
Use as seguintes peças de contexto para responder à pergunta no final.
Se você não souber a resposta, apenas diga que não sabe, não tente inventar uma resposta.
Use no máximo três frases e mantenha a resposta o mais concisa possível.
Sempre responda em português brasileiro.

{context}

Pergunta: {question}

Resposta em português brasileiro:
"""
