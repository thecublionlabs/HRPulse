import pandas as pd


def generate_department_salary_mart():
    employees_df = pd.read_csv(
        "data/staging/employees_cleaned.csv"
    )

    salary_df = pd.read_csv(
        "data/raw/salary.csv"
    )

    merged_df = pd.merge(
        employees_df,
        salary_df,
        on="employee_id",
        how="inner"
    )

    department_salary_df = (
        merged_df
        .groupby("department")
        .agg(
            employee_count=("employee_id", "count"),
            average_salary=("salary", "mean"),
            total_bonus=("bonus", "sum")
        )
        .reset_index()
    )

    print("\nDepartment Salary MART:")
    print(department_salary_df)

    department_salary_df.to_csv(
        "data/mart/department_salary_summary.csv",
        index=False
    )

    print(
        "\nDepartment salary MART saved successfully."
    )


if __name__ == "__main__":
    generate_department_salary_mart()