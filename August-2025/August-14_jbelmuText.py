"""
Jbelmud Text

Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

    The first and last letters of the words remain in place
    All letters between the first and last letter are sorted alphabetically.
    The input strings will contain no punctuation, and will be entirely lowercase.


"""

def jbelmu(text):

    words = text.split()
    processed_words = []

    for i in words:
        if len(i) <= 2:
            processed_words.append(i)
        else:
            first_letter = i[0]
            middle_letters = i[1:-1]
            last_letter = i[-1]

            sorted_middle = "".join(sorted(middle_letters))

            jumbled_output = first_letter + sorted_middle + last_letter
            processed_words.append(jumbled_output)
    final_word = " ".join(processed_words)
    return final_word
