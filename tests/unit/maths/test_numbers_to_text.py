from tasy_o.exercises.maths.numbers_to_text import _numbers_into_text
import pytest


@pytest.mark.anyio
async def test_numbers_into_text():
    # Given the input_str and the expected_result
    input_str = "42"
    expected_result = "FOUR TWO"

    # When transforming the numbers into text
    result = await _numbers_into_text(input_str)

    # Then the result must match with the expected_result
    assert result == expected_result


@pytest.mark.anyio
async def test_numbers_wrong_input():
    # Given the wrong_input
    wrong_input = "THIS IS WRONG"

    # When transofrming it into text
    with pytest.raises(KeyError):
        # Then the KeyError Exception is raised
        _ = await _numbers_into_text(wrong_input)
