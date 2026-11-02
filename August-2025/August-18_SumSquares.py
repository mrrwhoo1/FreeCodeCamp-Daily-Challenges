"""
Sum of Squares

Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.

"""


def sum_of_squares(n):
    nums = [*range(1, n + 1)]
    squared_nums = []

    total = 0
    for i in nums:
        squared_nums.append(i**2)
    for j in squared_nums:
        total += j

    return total
