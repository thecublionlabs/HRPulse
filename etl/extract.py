import pandas as pd
import json


def extract_employees():
    employees_df = pd.read_csv("data/raw/employees.csv")

    print("\nEmployees Data:")
    print(employees_df)

    return employees_df


def extract_salary():
    salary_df = pd.read_csv("data/raw/salary.csv")

    print("\nSalary Data:")
    print(salary_df)

    return salary_df


def extract_attendance():
    with open("data/raw/attendance.json", "r") as file:
        attendance_data = json.load(file)

    print("\nAttendance Data:")
    print(attendance_data)

    return attendance_data


def run_extraction_pipeline():
    extract_employees()
    extract_salary()
    extract_attendance()


if __name__ == "__main__":
    run_extraction_pipeline()