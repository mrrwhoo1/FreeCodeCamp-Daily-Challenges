"""
Targeted Sum

Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

    The returned array should have the indices in ascending order.


"""


def find_target(arr, target):

    seen = {}

    for Index, Value in enumerate(arr):
        difference = target - Value
        if difference in seen:
            return [seen[difference], Index]

        seen[Value] = Index

    return "Target not found"


print(find_target([2, 7, 11, 15], 9))

"""
incase someone or myself ever reads this in the future and wonders why i subtracted and not added think of this:

2 + a = 9
so we make a the subject; a = 9-2 = 7

first iteration;
9-2=7
we add {2:0} to the dict
not 9-7=2, do we have 2 in the dict? yes so we get its value from the key in the dict
and the current index we are on which would be 1 so [0,1]
"""
