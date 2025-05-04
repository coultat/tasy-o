from tasy_o.models.maths import CalcSumCount, NumberToText


def test_calc_sum_count(calc_sum_count: CalcSumCount) -> None:
    # Given the input values ad the expected result
    input_values = calc_sum_count
    expected_divisibles = {2, 4, 6, 7, 8, 10, 12, 14}
    expected_sum = 63

    # When validating the input values
    result = CalcSumCount.model_validate(input_values)

    # Then the result must match with the expected result
    assert result.total_numbers == expected_divisibles
    assert result.sum_total_numbers == expected_sum


def test_numberst_to_text(number_to_text: dict[str, str]) -> None:
    # Given the input values and the expected result
    input_values = number_to_text
    expected_written_number = "SIX SEVEN"

    # When validating the input values
    result = NumberToText.model_validate(input_values)

    # Then the result must match with the expected result
    assert result.written_number == expected_written_number
