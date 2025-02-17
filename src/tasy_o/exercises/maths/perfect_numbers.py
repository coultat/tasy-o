"""A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding itself.
Proper divisors are the positive integers that divide the number exactly, excluding the number itself.
6 is a perfect number, it can only be divided by 3, 2 and 1
28 is another example and also 496
Write a function that calculates all the perfect numbers from 1 to n
"""

from fastapi import APIRouter, Depends
from tasy_o.api.validators import validate_number_int
from typing import Annotated


router = APIRouter(prefix="/maths", tags=["Maths"])


@router.get("/perfect_numbers")
async def find_perfect_numbers(
    top_limit: Annotated[int, Depends(validate_number_int)],
) -> dict[str, list[int]]:
    perfect_numbers = await _find_perfect_numbers(top_limit)
    return {"result": perfect_numbers}


async def _find_perfect_numbers(top_limit: int) -> list[int]:
    perfect_numbers: list[int] = []
    for i in range(2, top_limit):
        divisors = set()
        for j in range(1, i):
            if i % j == 0:
                divisors.add(j)
        if sum(divisors) == i:
            perfect_numbers.append(i)
    return perfect_numbers
