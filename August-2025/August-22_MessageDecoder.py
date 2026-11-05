"""
Message Decoder

Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

    A positive number means the message was shifted forward in the alphabet.
    A negative number means the message was shifted backward in the alphabet.
    Case matters, decoded characters should retain the case of their encoded counterparts.
    Non-alphabetical characters should not get decoded.


"""


# By far the only problem i still dont understand.


def decode(message, shift):
    decoded = ""

    for character in message:
        if character.isalpha():
            if character.isupper():
                start = ord("A")
            else:
                start = ord("a")

            position = ord(character) - start
            new_position = (position - shift) % 26

            decoded += chr(start + new_position)
        else:
            decoded += character

    return decoded


print(decode("Xlmw mw e wigvix qiwweki.", 4))
