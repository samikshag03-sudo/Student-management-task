"""Small input validators."""
import re


def is_valid_email(email: str) -> bool:
    if not email:
        return True
    # Simple regex - good enough for demo
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def assert_non_empty_str(value: str, name: str) -> None:
    if not value or not value.strip():
        raise ValueError(f"{name} cannot be empty.")


def assert_positive_int(value: int, name: str) -> None:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer.")
