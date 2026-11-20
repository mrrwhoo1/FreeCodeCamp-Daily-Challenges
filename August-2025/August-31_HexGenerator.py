"""
Hex Generator

Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

    The function should handle "red", "green", or "blue" as an input argument.
    If the input is not one of those, the function should return "Invalid color".
    The function should return a random six-character hex color code where the input color value is greater than any of the others.

"""
import random

def generate_hex(color):
    if color not in ("red", "green", "blue"):
        return "Invalid color"

    dominant = random.randint(1, 255)
    other_one = random.randint(0, dominant - 1)
    other_two = random.randint(0, dominant - 1)

    if color == "red":
        red, green, blue = dominant, other_one, other_two
    elif color == "green":
        red, green, blue = other_one, dominant, other_two
    else:
        red, green, blue = other_one, other_two, dominant

    return f"{red:02X}{green:02X}{blue:02X}"

print(generate_hex("red"))
print(generate_hex("purple"))