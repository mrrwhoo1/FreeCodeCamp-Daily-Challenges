"""
Character Battle

Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

    Characters a-z have a strength of 1-26, respectively.
    Characters A-Z have a strength of 27-52, respectively.
    Digits 0-9 have a strength of their face value.
    All other characters have a value of zero.
    Each character can only fight one battle.

For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:

    "Opponent retreated" if your army has more characters than the opposing army.
    "We retreated" if the opposing army has more characters than yours.
    "We won" if your army won more battles.
    "We lost" if the opposing army won more battles.
    "It was a tie" if both armies won the same number of battles.


"""


def battle(my_army, opposing_army):

    # ----------This part is just setting up the dict
    all_characters = (
        [chr(i) for i in range(97, 123)]
        + [chr(i) for i in range(65, 91)]
        + [*range(10)]
    )

    char_values = [*range(1, 53)]

    characters = dict(zip(all_characters, char_values))

    digit_values = [str(i) for i in range(10)]

    for digit in digit_values:
        characters[digit] = int(digit)

    # Actual Problem solving.

    my_wins = 0
    opponent_wins = 0

    for my_character, opponent_character in zip(my_army, opposing_army):
        my_strength = characters.get(my_character, 0)
        opponent_strength = characters.get(opponent_character, 0)

        if my_strength > opponent_strength:
            my_wins += 1

        elif my_strength < opponent_strength:
            opponent_wins += 1

    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    if len(my_army) < len(opposing_army):
        return "We retreated"
    if my_wins > opponent_wins:
        return "We won"
    if my_wins < opponent_wins:
        return "We lost"
    if my_wins == opponent_wins:
        return "It was a tie"
