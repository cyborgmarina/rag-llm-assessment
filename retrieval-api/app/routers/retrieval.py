from fastapi import APIRouter, HTTPException, status
from app.models import Query, Response
from app.services import AugmentedRetrievalService

router = APIRouter()
augmented_retrieval_service = AugmentedRetrievalService()


@router.post("/retrieval", response_model=Response, status_code=status.HTTP_201_CREATED)
async def retrieve_context(query: Query):
    try:
        response = augmented_retrieval_service.generate_response_from_knowledge_base(
            query.question
        )
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e)
        )


@router.get("/retrieval", status_code=status.HTTP_200_OK)
async def retrieve_all_responses():
    responses = augmented_retrieval_service.get_generated_responses()
    return responses
