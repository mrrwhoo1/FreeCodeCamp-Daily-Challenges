"""


Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

    The string can contain any characters.
    The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
    If there's an odd number of characters in the string, ignore the center character.


"""

def is_balanced(s):
    s=s.lower()
    vowels = ['a','e','i','o','u']
    first_dict = {}
    second_dict = {}
    if len(s)%2==0:
        mid = len(s)//2
        first_half = s[:mid]
        second_half = s[mid:]
        for v in vowels:
            first_dict[v] = first_half.count(v)
            second_dict[v] = second_half.count(v)
        sum_first =sum(first_dict.values())
        sum_second =sum(second_dict.values())
        if sum_first == sum_second:
            return True
        else:
            return False

    else:
            mid = len(s)//2
            first_half = s[:mid]
            second_half = s[mid+1:]
            for v in vowels:
                first_dict[v] = first_half.count(v)
                second_dict[v] = second_half.count(v)
            sum_first =sum(first_dict.values())
            sum_second =sum(second_dict.values())
            if sum_first == sum_second:
                return True
            else:
                return False



