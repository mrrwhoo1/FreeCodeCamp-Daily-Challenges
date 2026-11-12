"""
Second Best

Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

    The second-most expensive laptop in the list if it is within your budget, or
    The most expensive laptop you can afford otherwise, or
    0 if no laptops are within your budget.

    Duplicate prices should be ignored.


"""


def get_laptop_cost(laptops, budget):

    prices = sorted(set(laptops))
    second_highest = prices[-2]

    if budget >= second_highest:
        return second_highest

    affordable = [p for p in prices if p <= budget]

    return max(affordable) if affordable else 0
