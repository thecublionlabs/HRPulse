from pydantic import BaseModel


class PipelineRequest(BaseModel):
    file_name: str
    department: str
    run_validation: bool