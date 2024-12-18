from fastapi import APIRouter, HTTPException, Depends
from app.models.design import DesignRequest, DesignResponse
from app.services.ai_service import AIService
from app.dependencies import get_ai_service

router = APIRouter()


@router.post("/generate", response_model=DesignResponse)
async def generate_design(
    request: DesignRequest,
    ai_service: AIService = Depends(get_ai_service),
) -> DesignResponse:
    try:
        content = await ai_service.generate_design_doc(
            request.prev_design, request.messages, request.model
        )
        return DesignResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
