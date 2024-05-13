from fastapi import APIRouter, HTTPException, status
from app.models import Query, Response
from app.database import search_documents

router = APIRouter()

@router.post("/retrieval", response_model=Response, status_code=status.HTTP_201_CREATED)
async def retrieve_context(query: Query):
    try:
        context = search_documents(query.question)
        # Placeholder for calling the LLM API
        assistant_response = "This is a generated response from the LLM"
        return Response(context=context, assistantResponse=assistant_response)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))

