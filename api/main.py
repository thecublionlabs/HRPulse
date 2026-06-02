from configs.app_config import (
    get_app_name,
    get_app_env
)
from api.routes.pipeline import (
    router as pipeline_router
)
from api.routes.employees import (
    router as employee_router
)
from api.routes.health import router as health_router
from etl.run_pipeline import run_pipeline
import pandas as pd
from fastapi import FastAPI

app = FastAPI(
    title=get_app_name(),
    description="HRPulse HR Data Platform",
    version="1.0.0"
)

app.include_router(
    health_router
)
app.include_router(
    employee_router
)
app.include_router(
    pipeline_router
)
@app.get("/")
def home():

    return {
        "application": get_app_name(),
        "environment": get_app_env(),
        "status": "running",
        "phase": "Phase 2"
    }
@app.get("/department-summary")
def department_summary():

    mart_df = pd.read_csv(
        "data/mart/department_salary_summary.csv"
    )

    return mart_df.to_dict(
        orient="records"
    )
@app.post("/run-pipeline")
def run_hr_pipeline():

    run_pipeline()

    return {
        "status": "success",
        "message": "HRPulse pipeline executed"
    }