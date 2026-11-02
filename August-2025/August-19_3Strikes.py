"""
3 Strikes

Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.
"""


def squares_with_three(n):

    nums = [*range(1, n + 1)]

    total = 0
    for i in nums:
        square = i**2
        if "3" in str(square):
            total += 1
    return total
