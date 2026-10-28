"""
Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

    Your function should handle sequences of any length greater than or equal to zero.
    If the length is zero, return an empty array.
    Note that the starting numbers are part of the sequence.


"""


def fibonacci_sequence(start_sequence, length):

    return_values = start_sequence.copy()

    if length == 1:
        return [return_values[0]]
    if length == 0:
        return []

    while len(return_values) < length:
       next_value = return_values[-1] + return_values[-2]
       return_values.append(next_value)
    return return_values
print(fibonacci_sequence([0,1,2], 20))

