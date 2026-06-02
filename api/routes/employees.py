from fastapi import APIRouter, HTTPException
import pandas as pd

router = APIRouter(
    tags=["Employees"]
)


@router.get("/employee/{employee_id}")
def get_employee(employee_id: str):

    employees_df = pd.read_csv(
        "data/raw/employees.csv"
    )

    employee_df = employees_df[
        employees_df["employee_id"] == employee_id
    ]

    if employee_df.empty:

        raise HTTPException(
        status_code=404,
        detail=f"Employee {employee_id} not found"
    )

    return employee_df.to_dict(
        orient="records"
    )[0]