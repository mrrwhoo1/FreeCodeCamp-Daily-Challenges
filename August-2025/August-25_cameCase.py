"""
camelCase

Given a string, return its camel case version using the following rules:

    Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
    The first word should be all lowercase.
    Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
    All spaces and separators should be removed.


"""


def to_camel_case(text):

    text = text.replace("-", " ").replace("_", " ")

    words = text.split()

    result = words[0].lower()

    for word in words[1:]:
        result += word.capitalize()

    return result
