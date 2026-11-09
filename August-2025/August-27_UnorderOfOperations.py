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
