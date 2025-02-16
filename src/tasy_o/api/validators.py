from fastapi import HTTPException


def validate_number_str(input_number: str) -> str:
    if not input_number.isdigit():
        raise HTTPException(status_code=400, detail="Invalid input: only string digits")
    return input_number


def validate_number_int(input_number: str) -> int:
    if not input_number.isdigit():
        raise HTTPException(status_code=400, detail="Invalid input: only ints")
    return int(input_number)