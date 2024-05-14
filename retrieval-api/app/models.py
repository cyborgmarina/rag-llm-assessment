from pydantic import BaseModel
from typing import List, Optional


class Query(BaseModel):
    question: str


class Response(BaseModel):
    context: Optional[str] = None
    assistantResponse: str
