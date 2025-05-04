from .conftest import client


def test_calc_sum_count():
    # Given the endpoint, the query parameters, the input
    # the expected result and the client
    endpoint = "/maths/maths/calc_sum_count"
    input_number = 13
    query_parameters = f"?input_number={input_number}"
    expected_result = {
        "result": {
            "total_numbers": [2, 4, 6, 7, 8, 10, 12],
            "sum_total_numbers": 49,
        }
    }

    # When calling the endpoint
    response = client.get(endpoint + query_parameters)

    # Then the result must match
    assert (
        response.json()["result"]["divisibles"]
        == expected_result["result"]["total_numbers"]
    )
    assert (
        response.json()["result"]["suma_divisibles"]
        == expected_result["result"]["sum_total_numbers"]
    )


def test_calc_sum_count_wrong_input():
    # Given the endpoint, the query parameters, the input
    endpoint = "/maths/maths/calc_sum_count"
    input_number = "listen to Rival Sons, they are good thing!"
    query_parameters = f"?input_number={input_number}"
    expected_status_code = 400
    expected_result = {"detail": "Invalid input: only ints"}

    # When calling the endpoint
    response = client.get(endpoint + query_parameters)

    # Then the result must match
    assert response.status_code == expected_status_code
    assert response.json() == expected_result
