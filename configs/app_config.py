from dotenv import load_dotenv
import os

load_dotenv()


def get_app_name():
    return os.getenv(
        "APP_NAME",
        "HRPulse"
    )


def get_app_env():
    return os.getenv(
        "APP_ENV",
        "development"
    )


def get_log_level():
    return os.getenv(
        "LOG_LEVEL",
        "INFO"
    )