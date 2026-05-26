from etl.mart import (
    generate_department_salary_mart
)

from configs.logger_config import setup_logger
logger = setup_logger()

from etl.extract import (
    extract_employees,
    extract_salary,
    extract_attendance
)

from etl.transform import (
    transform_employees
)

from etl.validate import (
    validate_employees
)


def run_pipeline():
    logger.info("HRPulse ETL Pipeline Started")
    logger.info("=" * 50)

    logger.info("STEP 1 — EXTRACTION")
    logger.info("-" * 50)

    extract_employees()
    extract_salary()
    extract_attendance()

    logger.info("STEP 2 — TRANSFORMATION")
    logger.info("-" * 50)

    transform_employees()

    logger.info("STEP 3 — VALIDATION")
    logger.info("-" * 50)

    validate_employees()
    print("\nSTEP 4 — MART GENERATION")
    print("-" * 50)

    generate_department_salary_mart()

    logger.info("HRPulse ETL Pipeline Completed")
    logger.info("=" * 50)
    

run_pipeline()