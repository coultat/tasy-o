import pytest
from typing import Union


@pytest.fixture
def calc_sum_count() -> dict[str, Union[set, int]]:
    return {
        "divisibles": {2, 4, 6, 8, 10, 12, 14, 7},
        "suma_divisibles": 63,
    }


@pytest.fixture
def number_to_text() -> dict[str, str]:
    return {
        "written_number": "SIX SEVEN",
    }
