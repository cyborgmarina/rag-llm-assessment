from fastapi import APIRouter, HTTPException, status
from app.models import Document
from app.database import documents

router = APIRouter()

@router.post("/document", status_code=status.HTTP_201_CREATED)
async def ingest_document(document: Document):
    if document.text in documents:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate text detected")
    documents.add(document.text)
    return {"message": "Document ingested successfully"}
