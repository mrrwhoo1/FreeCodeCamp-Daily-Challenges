# freeCodeCamp Daily Coding Challenges

My Python solutions to [freeCodeCamp's Daily Coding Challenges](https://www.freecodecamp.org/learn/daily-coding-challenge/).

I use this repository to keep track of the challenges I've completed and document how I approached each problem.

## Repository Structure

<details>
<summary>View repository structure</summary>

```text
FreeCodeCamp-Daily-Challenges/
├── README.md
└── August-2025/
    ├── August-11_VowelBalance.py
    ├── August-12_BaseCheck.py
    ├── August-13_FibonacciSequence.py
    ├── August-14_SPACEJAM.py
    ├── August-15_jbelmuText.py
    ├── August-16_AnagramChecker.py
    ├── August-17_TargetedSum.py
    ├── August-18_Factorializer.py
    ├── August-19_SumSquares.py
    ├── August-20_3Strikes.py
    ├── August-21_MilePace.py
    ├── August-22_MessageDecoder.py
    ├── August-23_UnaturalPrime.py
    ├── August-24_CharacterBattle.py
    ├── August-25_ReverseParenthesis.py
    ├── August-25_cameCase.py
    ├── August-27_UnorderOfOperations.py
    ├── August-28_SecondBest.py
    ├── August-29_CandleLight.py
    ├── August-30_ArrayDuplicates.py
    └── August-31_HexGenerator.py
```

</details>

## Table of Contents

- [About](#about)
- [Approach](#approach)
- [Progress](#progress)
- [Challenges](#challenges)
  - [August 11 – Vowel Balance](#august-11--vowel-balance)
  - [August 12 – Base Check](#august-12--base-check)
  - [August 13 – Fibonacci Sequence](#august-13--fibonacci-sequence)
  - [August 14 – SPACE JAM](#august-14--space-jam)
  - [August 15 – Jbelmud Text](#august-15--jbelmud-text)
  - [August 16 – Anagram Checker](#august-16--anagram-checker)
  - [August 17 – Targeted Sum](#august-17--targeted-sum)
  - [August 18 – Factorializer](#august-18--factorializer)
  - [August 19 – Sum of Squares](#august-19--sum-of-squares)
  - [August 20 – 3 Strikes](#august-20--3-strikes)
  - [August 21 – Mile Pace](#august-21--mile-pace)
  - [August 22 – Message Decoder](#august-22--message-decoder)
  - [August 23 – Unnatural Prime](#august-23--unnatural-prime)
  - [August 24 – Character Battle](#august-24--character-battle)
  - [August 25 – Reverse Parentheses](#august-25--reverse-parentheses)
  - [August 25 – Camel Case](#august-25--camel-case)
  - [August 27 – Order of Operations](#august-27--order-of-operations)
  - [August 28 – Second Best](#august-28--second-best)
  - [August 29 – Candlelight](#august-29--candlelight)
  - [August 30 – Array Duplicates](#august-30--array-duplicates)
  - [August 31 – Hex Generator](#august-31--hex-generator)

## About

This repository contains my solutions to the daily Python coding challenges from freeCodeCamp.

The goal is to practise problem-solving, strengthen my Python fundamentals, and become more comfortable working with different programming concepts.

## Approach

I focus on understanding each problem before writing a solution. I also try to use approaches I understand and can explain rather than choosing a complicated solution just because it is shorter or more advanced.

Each challenge includes a brief explanation of the approach used and why I chose it.

## Progress

| Category | Details |
|---|---|
| Challenges completed | 21 |
| Challenge period | August 2025 |
| Language | Python |
| Status | In progress |

---

# Challenges

## August 11 – Vowel Balance

**File:** [`August-11_VowelBalance.py`](August-2025/August-11_VowelBalance.py)

### Approach
Convert the string to lowercase and divide it into two halves. Count the vowels in each half using dictionaries, then compare the totals.

For strings with an odd number of characters, the middle character is excluded from the comparison.

### Why I Chose This Approach
Splitting the string makes it easier to compare both sides independently. Dictionaries provide a straightforward way to keep track of vowel counts.

## August 12 – Base Check

**File:** [`August-12_BaseCheck.py`](August-2025/August-12_BaseCheck.py)

### Approach
Create collections containing digits and letters, then use the requested base to determine which characters are valid.

Convert each character to uppercase before checking whether it belongs to the allowed characters for that base.

### Why I Chose This Approach
Using a collection of valid characters makes the validation process simple and avoids having to write separate conditions for every possible base.

## August 13 – Fibonacci Sequence

**File:** [`August-13_FibonacciSequence.py`](August-2025/August-13_FibonacciSequence.py)

### Approach
Start with the initial Fibonacci numbers and repeatedly append the sum of the last two numbers until the required sequence length is reached.

Handle cases where the requested length is zero or one separately.

### Why I Chose This Approach
A list makes it easy to access the previous two numbers and build the sequence one value at a time.

## August 14 – SPACE JAM

**File:** [`August-14_SPACEJAM.py`](August-2025/August-14_SPACEJAM.py)

### Approach
Remove spaces from the original string, convert the remaining characters to uppercase, and join them with two spaces between each character.

### Why I Chose This Approach
Python's string methods make this transformation straightforward without needing to manually construct the result character by character.

## August 15 – Jbelmud Text

**File:** [`August-15_jbelmuText.py`](August-2025/August-15_jbelmuText.py)

### Approach
Split the text into individual words. Keep the first and last characters of each word unchanged while sorting the characters in between.

Reconstruct the words and join them back into a sentence.

### Why I Chose This Approach
Working with individual words makes it easier to manipulate their middle characters without changing their outer characters.

## August 16 – Anagram Checker

**File:** [`August-16_AnagramChecker.py`](August-2025/August-16_AnagramChecker.py)

### Approach
Remove spaces and convert both strings to lowercase. Sort the characters in each string and compare the resulting lists.

### Why I Chose This Approach
Sorting places the same characters in the same order when two strings are anagrams, making comparison simple.

## August 17 – Targeted Sum

**File:** [`August-17_TargetedSum.py`](August-2025/August-17_TargetedSum.py)

### Approach
Use a dictionary to store numbers that have already been visited alongside their indexes.

For each number, calculate the difference between the target and the current number. Check whether that difference already exists in the dictionary.

If it does, return the two indexes.

### Why I Chose This Approach
A dictionary allows previously encountered numbers to be looked up efficiently without repeatedly checking every possible pair.

## August 18 – Factorializer

**File:** [`August-18_Factorializer.py`](August-2025/August-18_Factorializer.py)

### Approach
Start with a result variable initialized to `1`. Loop through the required numbers and multiply each one into the running result.

### Why I Chose This Approach
A simple loop makes the factorial calculation easy to follow and avoids unnecessary complexity.

## August 19 – Sum of Squares

**File:** [`August-19_SumSquares.py`](August-2025/August-19_SumSquares.py)

### Approach
Create a list containing the square of each number. Then loop through that list and add the values together.

### Why I Chose This Approach
Separating the squaring and addition steps makes the process easier to understand and follow.

## August 20 – 3 Strikes

**File:** [`August-20_3Strikes.py`](August-2025/August-20_3Strikes.py)

### Approach
Loop through the required range of numbers, square each number, and convert the result to a string.

Check whether the resulting string contains the character `"3"`.

### Why I Chose This Approach
Converting the squared number to a string allows the program to check for a particular digit using a simple membership test.

## August 21 – Mile Pace

**File:** [`August-21_MilePace.py`](August-2025/August-21_MilePace.py)

### Approach
Separate the minutes and seconds, convert the pace into total seconds, and divide by the number of miles.

Convert the result back into minutes and seconds, using zero-padding where necessary.

### Why I Chose This Approach
Performing the calculation in seconds avoids complications when dividing minutes and seconds separately.

## August 22 – Message Decoder

**File:** [`August-22_MessageDecoder.py`](August-2025/August-22_MessageDecoder.py)

### Approach
Loop through each character in the message. Use `ord()` and `chr()` to shift alphabetic characters by the required amount.

Apply modulo 26 to keep the shifted character within the alphabet and preserve the original letter's case. Leave non-alphabetic characters unchanged.

### Why I Chose This Approach
Working with character codes makes it possible to shift letters mathematically without creating a separate lookup table.

## August 23 – Unnatural Prime

**File:** [`August-23_UnaturalPrime.py`](August-2025/August-23_UnaturalPrime.py)

### Approach
Convert negative numbers to their positive equivalents, then reject values smaller than 2.

Loop through possible divisors and check whether the number can be divided evenly. If a divisor is found, the number is not prime.

### Why I Chose This Approach
Checking divisibility is a direct way to determine whether a number has factors other than 1 and itself.

## August 24 – Character Battle

**File:** [`August-24_CharacterBattle.py`](August-2025/August-24_CharacterBattle.py)

### Approach
Create a dictionary assigning strength values to lowercase letters, uppercase letters, and digits.

Use `zip()` to compare characters at corresponding positions in both armies. Retrieve their strengths using dictionary lookups and count the wins.

Finally, compare army sizes to determine whether either army retreats before checking the battle results.

### Why I Chose This Approach
A dictionary keeps the character strength values organized, while `zip()` makes it easy to compare corresponding characters without manually managing indexes.

## August 25 – Reverse Parentheses

**File:** [`August-25_ReverseParenthesis.py`](August-2025/August-25_ReverseParenthesis.py)

### Approach
Use a `while` loop to process the string until no opening parentheses remain.

Use `rfind()` to locate the innermost opening parenthesis, find its matching closing parenthesis, and reverse the text between them using slicing (`[::-1]`).

Rebuild the string without those parentheses and repeat the process.

### Why I Chose This Approach
Processing the innermost parentheses first makes nested parentheses easier to handle. String slicing also provides a simple way to reverse the selected section.

## August 25 – Camel Case

**File:** [`August-25_cameCase.py`](August-2025/August-25_cameCase.py)

### Approach
Replace hyphens and underscores with spaces, then split the string into words.

Convert the first word to lowercase and capitalize the first character of each remaining word. Join everything together without spaces.

### Why I Chose This Approach
Breaking the string into words makes it easier to apply different capitalization rules to the first word and the remaining words.

## August 27 – Order of Operations

**File:** [`August-27_UnorderOfOperations.py`](August-2025/August-27_UnorderOfOperations.py)

### Approach
Start with the first number as the running total. Process the remaining numbers from left to right, applying the operators in their given order.

Use an index to cycle through the operators and reset it when necessary. Division uses floor division (`//`).

### Why I Chose This Approach
A running total allows each operation to build on the previous result without needing to create separate calculations for every operator.

## August 28 – Second Best

**File:** [`August-28_SecondBest.py`](August-2025/August-28_SecondBest.py)

### Approach
Remove duplicate laptop prices using `set()` and sort the remaining values.

Find the second-highest distinct price. If it exceeds the budget, search for the highest affordable price instead. Return `0` if no suitable option exists.

### Why I Chose This Approach
Using a set removes duplicate prices, while sorting makes it easier to identify the highest and second-highest values.

## August 29 – Candlelight

**File:** [`August-29_CandleLight.py`](August-2025/August-29_CandleLight.py)

### Approach
Keep track of the total number of candles burned and the number of leftover candles.

Inside a `while` loop, burn the available candles and add their leftovers to the running total. Use integer division (`//`) to calculate how many new candles can be made and modulo (`%`) to calculate the remaining leftovers.

Continue until there are no more candles to burn.

### Why I Chose This Approach
A loop naturally represents the recycling process because each batch of new candles can be burned to produce more leftovers.

## August 30 – Array Duplicates

**File:** [`August-30_ArrayDuplicates.py`](August-2025/August-30_ArrayDuplicates.py)

### Approach
Create a set of unique values from the original array. Loop through those values and use `count()` to identify which ones appear more than once.

Sort the resulting list of duplicates before returning it.

### Why I Chose This Approach
Using a set prevents checking the same value multiple times, while `count()` makes it easy to identify repeated elements.

## August 31 – Hex Generator

**File:** [`August-31_HexGenerator.py`](August-2025/August-31_HexGenerator.py)

### Approach
Validate the requested dominant color (`red`, `green`, or `blue`).

Generate a random value between 1 and 255 for the dominant channel, then generate two smaller values for the remaining channels.

Arrange the three values in RGB order according to the requested dominant color. Format each channel using `:02X` and combine them into a six-character hexadecimal color.

### Why I Chose This Approach
Generating the RGB values separately makes it easier to control which color dominates. Python's hexadecimal formatting handles the conversion and ensures each channel occupies exactly two characters.

---

## License

This repository is primarily a personal learning archive of my solutions to freeCodeCamp's Daily Coding Challenges.
