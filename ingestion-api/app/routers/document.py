from fastapi import APIRouter, HTTPException, UploadFile, File, status
from app.models import Document
from app.services import DocumentService
from typing import List

router = APIRouter()
document_service = DocumentService()


@router.post("/document", status_code=status.HTTP_201_CREATED)
async def ingest_document(file: UploadFile = File(...)):
    if file.content_type != "text/plain":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only plain text files are supported",
        )

    content = await file.read()

    document = Document(text=content.decode("utf-8"))

    try:
        chunks_count = document_service.add_document(document)
        return {
            "message": f"Document ingested successfully. {chunks_count} chunks added to vectordb."
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
