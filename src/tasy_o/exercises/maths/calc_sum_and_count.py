"""
"Create a function named calc_sum_and_count_all_numbers_div_by_2_or_7 that:
Iterates from 1 to a defined maximum number.
Counts how many numbers between 0 and the maximum are divisible by 2 or 7.
Also calculates the sum of those numbers.

Example:
For the number 15:
Divisible by 2: 2, 4, 6, 8, 10, 12, 14
Divisible by 7: 7, 14
Total numbers: [2, 4, 6, 8, 10, 12, 14, 7] (count: 8)
Sum of these numbers: 63."
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from tasy_o.api.validators import validate_number_int
from tasy_o.models.maths import CalcSumCount, ResponseMaths

router = APIRouter(prefix="/maths", tags=["Maths"])


@router.get("/calc_sum_count")
async def calc_sum_count(
    top_limit: Annotated[int, Depends(validate_number_int)],
) -> ResponseMaths:
    res = _calc_sum_and_count_all_numbers_div_by_2_or_7(top_limit)
    return ResponseMaths(result=res, message="Success")


def _calc_sum_and_count_all_numbers_div_by_2_or_7(max_choice: int) -> CalcSumCount:
    even_numbers = []
    mult_seven = []
    for i in range(1, max_choice):
        if i % 2 == 0:
            even_numbers.append(i)
        if i % 7 == 0:
            mult_seven.append(i)
    total_numbers = {*even_numbers, *mult_seven}
    sum_total_numbers = sum(total_numbers)
    return CalcSumCount(divisibles=total_numbers, suma_divisibles=sum_total_numbers)
