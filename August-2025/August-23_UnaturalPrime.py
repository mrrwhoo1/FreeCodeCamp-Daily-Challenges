"""
Unnatural Prime

Given an integer, determine if that number is a prime number or a negative prime number.

    A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
    A negative prime number is the negative version of a positive prime number.
    1 and 0 are not considered prime numbers.


"""


def is_unnatural_prime(n):
    str_num = str(n)
    remove_neg = str_num.replace("-", "")
    number = int(remove_neg)

    devisors = range(2, number)

    if number < 2:
        return False

    for possible_devisor in devisors:
        if int(remove_neg) % possible_devisor == 0:
            return False
    return True
