from fastapi import APIRouter
from .perfect_numbers import router as perfect_numbers_router
from .numbers_to_text import router as numbers_into_text_router
from .calc_sum_and_count import router as calc_sum_count


maths_router = APIRouter(prefix="/maths", tags=["Maths"])


maths_router.include_router(perfect_numbers_router)
maths_router.include_router(numbers_into_text_router)

maths_router.include_router(calc_sum_count)
