from api.models.pipeline_models import (
    PipelineRequest
)
from fastapi import APIRouter

router = APIRouter(
    tags=["Pipeline"]
)


@router.post("/pipeline-request")
def pipeline_request(
    request: PipelineRequest
):

    return {
        "file_name": request.file_name,
        "department": request.department,
        "run_validation": request.run_validation
    }