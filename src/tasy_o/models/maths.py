from pydantic import BaseModel, Field
from typing import TypeVar, Generic


class CalcSumCount(BaseModel):
    total_numbers: set | None = Field(default=None, alias="divisibles")
    sum_total_numbers: int | None = Field(default=None, alias="suma_divisibles")


class NumberToText(BaseModel):
    written_number: str | None


MathsResponse = TypeVar("MathsResponse", NumberToText, CalcSumCount)


class ResponseMaths(BaseModel, Generic[MathsResponse]):
    result: MathsResponse
    message: str | None = Field(default=None)
    status_code: int | None = Field(default=200, alias="status")
