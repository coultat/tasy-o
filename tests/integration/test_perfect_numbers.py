from .conftest import client


def test_perfect_numbers():
    # Given the endpoint, the query parameters, the input
    # the expected result and the client
    endpoint = "/maths/maths/perfect_numbers"
    input_number = '42'
    query_parameters = f"?input_number={input_number}"
    expected_result = [6, 28]  # Should be a set but FastAPI doesn't serialize sets
    expected_status_response = 200

    # When calling the endpoint
    response = client.get(endpoint + query_parameters)

    # Then the result must match
    assert expected_result == response.json()['result']


def test_perfect_numbers_wrong():
    # Given the endpoint, the query parameters, the input
    # the expected result and the client
    endpoint = "/maths/maths/perfect_numbers"
    input_number = 'fourty two'
    query_parameters = f"?input_number={input_number}"
    expected_result = {'detail': 'Invalid input: only ints'}

    # When finding perfect numbers
    result = client.get(endpoint + query_parameters)

    # Then the result must match with the expected result
    assert result.status_code == 400
    assert result.json() == expected_result
