def sum_of_squares(numbers):
    """
    Returns the sum of the squares of the numbers in the provided list.

    Args:
        numbers (list): A list of numbers (int or float).

    Returns:
        int or float: The sum of the squares of the input numbers.

    Example:
        >>> sum_of_squares([1, 2, 3])
        14
    """
    return sum(x ** 2 for x in numbers)

    
print(sum_of_squares([1, 2, 3]))

