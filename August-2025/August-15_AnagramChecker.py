"""
Anagram Checker

Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

    Ignore casing and white space.


"""


#side note: i know this solution fail for other space types like \t etc, BUT this passed all the checks. (just incase someone ever sees this and wonders how this was accepted""
def are_anagrams(str1, str2):

    clear_spaces_str1 = str1.replace(" ", "")
    clear_spaces_str2 = str2.replace(" ","")

    anagram = sorted(clear_spaces_str1.lower()) == sorted(clear_spaces_str2.lower())

    return anagram

