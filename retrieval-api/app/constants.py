from os import getenv

BASE_URL = getenv("BASE_URL", "https://openrouter.ai/api/v1")
CHAT_MODEL = getenv("CHAT_MODEL", "meta-llama/llama-3-8b-instruct:free")
API_KEY = getenv("API_KEY")

PROMPT_TEMPLATE = """
Use as seguintes peças de contexto para responder à pergunta no final.
Se você não souber a resposta, apenas diga que não sabe, não tente inventar uma resposta.
Use no máximo três frases e mantenha a resposta o mais concisa possível.
Sempre responda em português brasileiro.

{context}

Pergunta: {question}

Resposta em português brasileiro:
"""
