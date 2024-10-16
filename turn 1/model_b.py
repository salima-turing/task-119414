# Importing required modules
import pytest
from unittest.mock import MagicMock

# Dummy data for testing
DATA_RESIDENCY_REQUIREMENTS = {
    "country": "US",
    "state": "California",
    "city": "San Francisco",
}


# Function to be tested
def check_data_residency(data, residency_policy):
    """
    Function to check if the data adheres to the data residency policy.
    """
    for key, value in data.items():
        if key in residency_policy and residency_policy[key] != value:
            return False
    return True


@pytest.mark.parametrize("data, expected_result", [
    # BVA - Testing with boundary values
    ({}, True),  # Empty data
    ({"country": "US"}, True),  # Partial data with valid country
    ({"country": "IN"}, False),  # Invalid country
    # Equivalence Partitioning - Testing different country values
    ({"country": "US"}, True),
    ({"country": "US", "state": "California"}, True),
    ({"country": "US", "state": "Invalid"}, False),
    ({"country": "IN"}, False),
])
def test_check_data_residency_boundary_values(data, expected_result):
    """
    Test check_data_residency function with boundary values.
    """
    assert check_data_residency(data, DATA_RESIDENCY_REQUIREMENTS) == expected_result


@pytest.mark.parametrize("data, expected_result", [
    # Decision Table Testing - Testing different combinations of input data
    ({"country": "US", "state": "California", "city": "San Francisco"}, True),  # Valid data
    ({"country": "US", "state": "Invalid", "city": "San Francisco"}, False),  # Invalid state
    ({"country": "US", "state": "California", "city": "Invalid"}, False),  # Invalid city
    ({"country": "IN", "state": "Invalid", "city": "Invalid"}, False),  # Invalid country and state
])
def test_check_data_residency_decision_table(data, expected_result):
    """
    Test check_data_residency function using decision table.
    """
    assert check_data_residency(data, DATA_RESIDENCY_REQUIREMENTS) == expected_result


def test_check_data_residency_mock_objects():
    """
    Test check_data_residency function using mock objects.
    """
    # Mocking the data storage service
    mock_data_storage = MagicMock()
    mock_data_storage.get_data.return_value = {"country": "US"}

    # Testing with the mocked data storage service
    assert check_data_residency(mock_data_storage.get_data(), DATA_RESIDENCY_REQUIREMENTS) == True


if __name__ == "__main__":
    pytest.main()
