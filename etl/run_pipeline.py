from extract import (
    extract_employees,
    extract_salary,
    extract_attendance
)

from transform import (
    transform_employees
)

from validate import (
    validate_employees
)


def run_pipeline():
    print("\nHRPulse ETL Pipeline Started")
    print("=" * 50)

    print("\nSTEP 1 — EXTRACTION")
    print("-" * 50)

    extract_employees()
    extract_salary()
    extract_attendance()

    print("\nSTEP 2 — TRANSFORMATION")
    print("-" * 50)

    transform_employees()

    print("\nSTEP 3 — VALIDATION")
    print("-" * 50)

    validate_employees()

    print("\nHRPulse ETL Pipeline Completed")
    print("=" * 50)


run_pipeline()