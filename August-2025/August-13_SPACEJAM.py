"""
Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.
Non-alphabetical characters should remain unchanged (except for spaces).
"""


def space_jam(s):
    remove_spaces = s.strip().replace(" ", "")
    to_upper = remove_spaces.upper()
    insert_spaces = "  ".join(to_upper)
    return insert_spaces
print(space_jam("freeCodeCamp"))
