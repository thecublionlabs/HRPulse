import pandas as pd


def transform_employees():
    employees_df = pd.read_csv("data/raw/employees.csv")

    print("\nOriginal Employee Count:")
    print(len(employees_df))

    # Remove duplicate rows
    employees_df = employees_df.drop_duplicates()

    # Standardize department names
    employees_df["department"] = employees_df["department"].str.title()

    print("\nEmployee Count After Removing Duplicates:")
    print(len(employees_df))

    print("\nRows With Missing Values:")
    print(employees_df[employees_df.isnull().any(axis=1)])

    print("\nTransformed Employee Data:")
    print(employees_df)

    employees_df.to_csv(
        "data/staging/employees_cleaned.csv",
        index=False
    )

    print("\nCleaned employee data saved to staging layer.")


if __name__ == "__main__":
    transform_employees()