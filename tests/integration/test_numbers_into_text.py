from .conftest import client


def test_numbers_into_text():
    # Given the endpoint, the query parameters
    # the input, the expected_result and the client
    endpoint = "/maths/maths/numbers_into_text"
    input_number = "42"
    query_parameters = f"?input_number={input_number}"
    expected_result = {"result": "FOUR TWO"}
    expected_status_response = 200

    # When transforming the numbers into text
    response = client.get(endpoint + query_parameters)

    # Then the response must match with the expected result
    assert expected_result == response.json()
    assert expected_status_response == response.status_code


def test_numbers_into_txt_wrong():
    # Given the endpoint, the query parameters
    # the input, the expected_result and the client
    endpoint = "/maths/maths/numbers_into_text"
    input_number = "Fourty two"
    query_parameters = f"?input_number={input_number}"
    expected_result = {"detail": "Invalid input: only string digits"}
    expected_status_response = 400

    response = client.get(endpoint + query_parameters)

    assert response.json() == expected_result
    assert response.status_code == expected_status_response
