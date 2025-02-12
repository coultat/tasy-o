"""
Write a function that converts numbers into text.
7 will be SEVEN, 55 will be FIVE FIVE
"""
from fastapi import APIRouter


router = APIRouter(prefix="/maths", tags=["Maths"])

@router.get("/numbers_into_text")
async def numbers_into_text(input_number: str) -> str:
    numbers_dict = {"1": "ONE",
                    "2": "TWO",
                    "3": "THREE",
                    "4": "FOUR",
                    "5": "FIVE",
                    "6": "SIX",
                    "7": "SEVEN",
                    "8": "EIGHT",
                    "9": "NINE",
                    "0": "ZERO"}
    result = ''
    for number in input_number:
        result += f"{numbers_dict[number]} "
    return result.strip()