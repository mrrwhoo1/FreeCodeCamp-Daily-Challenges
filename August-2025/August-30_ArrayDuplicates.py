"""
Array Duplicates

Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

    Only include one instance of each value in the returned array.


"""


def find_duplicates(arr):

    duplicates = []

    for i in set(arr):
        if arr.count(i) > 1:
            duplicates.append(i)

    return sorted(duplicates)
