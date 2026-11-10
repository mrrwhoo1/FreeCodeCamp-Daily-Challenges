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
