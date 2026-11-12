"""
Unorder of Operations

Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

    Valid operators are +, -, *, /, and %.


"""


def evaluate(numbers, operators):

    total = numbers[0]

    operator_index = 0

    for i in range(1, len(numbers)):
        current_op = operators[operator_index]

        if current_op == "+":
            total = total + numbers[i]
        elif current_op == "%":
            total = total % numbers[i]
        elif current_op == "-":
            total = total - numbers[i]
        elif current_op == "*":
            total = total * numbers[i]
        elif current_op == "/":
            total = total // numbers[i]

        operator_index = operator_index + 1

        if operator_index >= len(operators):
            operator_index = 0

    return total
