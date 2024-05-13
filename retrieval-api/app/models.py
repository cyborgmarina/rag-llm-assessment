from pydantic import BaseModel
from typing import List

class Query(BaseModel):
    question: str

class Response(BaseModel):
    context: List[str]
    assistantResponse: str
