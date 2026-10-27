"""
Base Check

Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

    The string may contain digits and uppercase or lowercase letters.
    The check should be case-insensitive.
    A number is valid if every character is a valid digit in the given base.
    Examples of valid digits in different bases:
        Base 2: 0-1
        Base 8: 0-7
        Base 10: 0-9
        Base 16: 0-9 and A-F
        Base 36: 0-9 and A-Z


"""

def is_valid_number(n, base):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']

    bases = {}

    for b in range(2, 37):
        digits = nums[:min(b, 10)]
        extra_letters = letters[:max(0, b - 10)]
        bases[b] = digits + extra_letters

    if not n:
        return False

    for digit in n:
        if digit.upper() not in bases[base]:
            return False

    return True



