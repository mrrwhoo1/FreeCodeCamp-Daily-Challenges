
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



