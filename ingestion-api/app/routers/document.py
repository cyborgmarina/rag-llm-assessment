from fastapi import APIRouter, HTTPException, status
from app.models import Document
from app.services import DocumentService

router = APIRouter()

document_service = DocumentService()

@router.post("/document", status_code=status.HTTP_201_CREATED)
async def ingest_document(document: Document):
    try:
        document_service.add_document(document)
        return {"message": "Document ingested successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

