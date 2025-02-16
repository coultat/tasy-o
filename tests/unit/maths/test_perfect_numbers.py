from tasy_o.exercises.maths.perfect_numbers import find_perfect_numbers
import pytest


@pytest.mark.anyio
async def test_find_perfect_numbers():
    # Given the input_number and the expected result
    input_number = 40
    expected_result = {28, 6}

    # When finding the perfect numbers
    result = await find_perfect_numbers(input_number)

    # Then the result must match with the expected result
    assert result["result"] == expected_result


@pytest.mark.anyio
async def test_find_perfect_numbers_wrong_input():
    # Given the input
    input_number = "wrong input"

    # When finding the perfect numbers
    with pytest.raises(TypeError):
        _ = await find_perfect_numbers(input_number)

    # Then a TypeError must be raised
