# Assuming there's a function named 'add' in your project module
from my_project_module import add

def test_add_function():
    """
    Test the add function to ensure it returns the correct sum of two numbers.
    """
    # Arrange
    a = 2
    b = 3
    expected_sum = 5

    # Act
    result = add(a, b)

    # Assert
    assert result == expected_sum, f"Expected {expected_sum} but got {result}"
