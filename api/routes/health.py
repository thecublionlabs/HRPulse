from api.models.response_models import (
    HealthResponse
)
from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)


@router.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return {
        "status": "healthy",
        "service": "HRPulse API"
    }