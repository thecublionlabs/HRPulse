import pandas as pd


VALID_EMPLOYMENT_TYPES = [
    "Full-Time",
    "Contract"
]


def validate_employees():
    employees_df = pd.read_csv(
        "data/staging/employees_cleaned.csv"
    )

    print("\nVALIDATION REPORT")
    print("-" * 40)

    # Missing email validation
    missing_email_df = employees_df[
        employees_df["email"].isnull()
    ]

    print("\nEmployees Missing Email:")
    print(len(missing_email_df))

    if not missing_email_df.empty:
        print(missing_email_df)

    # Missing location validation
    missing_location_df = employees_df[
        employees_df["location"].isnull()
    ]

    print("\nEmployees Missing Location:")
    print(len(missing_location_df))

    if not missing_location_df.empty:
        print(missing_location_df)

    # Invalid employment type validation
    invalid_employment_df = employees_df[
        ~employees_df["employment_type"].isin(
            VALID_EMPLOYMENT_TYPES
        )
    ]

    print("\nInvalid Employment Types:")
    print(len(invalid_employment_df))

    if not invalid_employment_df.empty:
        print(invalid_employment_df)

    # Duplicate employee_id validation
    duplicate_employee_df = employees_df[
        employees_df.duplicated(
            subset=["employee_id"],
            keep=False
        )
    ]

    print("\nDuplicate Employee IDs:")
    print(len(duplicate_employee_df))

    if not duplicate_employee_df.empty:
        print(duplicate_employee_df)

    print("\nValidation Completed.")


validate_employees()