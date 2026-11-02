"""
Factorializer

Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.

    The factorial of zero is 1.

"""


def factorial(n):
    nums = [*range(1, n + 1)]

    total = 1
    for n in nums:
        total *= n

    return total


"""
for a 1 line shorter solution lol.
import math
result = math.prod(nums)
return result
"""
