"""
Decoder

Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:

    All characters inside each pair of parentheses should be reversed.
    Parentheses should be removed from the final result.
    If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
    Assume all parentheses are evenly balanced and correctly nested.

"""
def decode(s):
    while "(" in s:
        start = s.rfind("(")
        end = s.find(")", start)

        inside = s[start + 1:end]

        s = s[:start] + inside[::-1] + s[end + 1:]

    return s

print(decode("(ab(cd)ef)"))