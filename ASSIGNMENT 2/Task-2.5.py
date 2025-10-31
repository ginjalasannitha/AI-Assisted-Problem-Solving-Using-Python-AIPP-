def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a given list.
    Returns a tuple: (even_sum, odd_sum)
    """
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers.")

    even_sum = sum(x for x in numbers if x % 2 == 0)
    odd_sum = sum(x for x in numbers if x % 2 != 0)
    return even_sum, odd_sum

# Example test
print(sum_even_odd([1, 2, 3, 4, 5, 6]))  # Output: (12, 9)


 