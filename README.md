# FreeCodeCamp Daily Coding Challenges

My Python solutions to freeCodeCamp's Daily Coding Challenges. I use this repository to keep track of the challenges I've completed and how I approached each one.

## Repository Structure

<details>
<summary> Click to view the repository structure</summary>

<br />

```text
FreeCodeCamp-Daily-Challenges/
├── README.md
└── August-2025/
    ├── August-11_VowelBalance.py
    ├── August-12_BaseCheck.py
    ├── August-13_FibonacciSequence.py
    ├── August-13_SPACEJAM.py
    ├── August-14_jbelmuText.py
    ├── August-15_AnagramChecker.py
    ├── August-17_TargetedSum.py
    ├── August-18_Factorializer.py
    ├── August-19_SumSquares.py
    ├── August-20_3Strikes.py
    ├── August-21_MilePace.py
    ├── August-22_MessageDecoder.py
    ├── August-23_UnaturalPrime.py
    └── August-25_cameCase.py
```

</details>

## Table of Contents

| Section | Challenge | Solution |
|---|---|---|
| [About This Repository](#about-this-repository) | — | — |
| [My Problem-Solving Philosophy](#my-problem-solving-philosophy) | — | — |
| [Progress](#progress) | — | — |
| [August 11 — Vowel Balance](#august-11--vowel-balance) | Vowel Balance | [Python file](August-2025/August-11_VowelBalance.py) |
| [August 12 — Base Check](#august-12--base-check) | Base Check | [Python file](August-2025/August-12_BaseCheck.py) |
| [August 13 — Fibonacci Sequence](#august-13--fibonacci-sequence) | Fibonacci Sequence | [Python file](August-2025/August-13_FibonacciSequence.py) |
| [August 13 — Space Jam](#august-13--space-jam) | Space Jam | [Python file](August-2025/August-13_SPACEJAM.py) |
| [August 14 — Jbelmud Text](#august-14--jbelmud-text) | Jbelmud Text | [Python file](August-2025/August-14_jbelmuText.py) |
| [August 15 — Anagram Checker](#august-15--anagram-checker) | Anagram Checker | [Python file](August-2025/August-15_AnagramChecker.py) |
| [August 17 — Targeted Sum](#august-17--targeted-sum) | Targeted Sum | [Python file](August-2025/August-17_TargetedSum.py) |
| [August 18 — Factorializer](#august-18--factorializer) | Factorializer | [Python file](August-2025/August-18_Factorializer.py) |
| [August 19 — Sum of Squares](#august-19--sum-of-squares) | Sum of Squares | [Python file](August-2025/August-19_SumSquares.py) |
| [August 20 — 3 Strikes](#august-20--3-strikes) | 3 Strikes | [Python file](August-2025/August-20_3Strikes.py) |
| [August 21 — Mile Pace](#august-21--mile-pace) | Mile Pace | [Python file](August-2025/August-21_MilePace.py) |
| [August 22 — Message Decoder](#august-22--message-decoder) | Message Decoder | [Python file](August-2025/August-22_MessageDecoder.py) |
| [August 23 — Unnatural Prime](#august-23--unnatural-prime) | Unnatural Prime | [Python file](August-2025/August-23_UnaturalPrime.py) |
| [August 25 — Camel Case](#august-25--camel-case) | Camel Case | [Python file](August-2025/August-25_cameCase.py) |
| [Future Updates](#future-updates) | — | — |

## About This Repository

This repository contains my Python solutions to the daily challenges. I focus on writing code I understand and can explain, rather than choosing a complicated approach just because it is shorter or more advanced.

Each entry briefly describes how I approached the problem and why I chose that approach.

## My Problem-Solving Philosophy

I try to understand the problem first, then solve it using Python features I know how to use. My solutions may not always be the most efficient, but I want them to be readable and make sense to me. As I get more practice, I can revisit older solutions and improve them.

## Progress

- **Challenges completed:** 14
- **Language:** Python
- **Status:** In progress

---

## August 11 — Vowel Balance

**Solution:** [`August-11_VowelBalance.py`](August-2025/August-11_VowelBalance.py)

### Approach

I converted the string to lowercase, then split it into two halves. For strings with an odd number of characters, I excluded the middle character.

I used dictionaries to store the counts of `a`, `e`, `i`, `o`, and `u` in each half. I then summed the counts and compared the totals to determine whether the string was balanced.

### Why I Chose This Approach

I was comfortable with string slicing, loops, dictionaries, and Python's built-in `count()` method. Breaking the problem into separate steps made the logic easier for me to understand and verify.

I handled odd and even string lengths separately because that was the approach I could confidently implement at the time.

## August 12 — Base Check

**Solution:** [`August-12_BaseCheck.py`](August-2025/August-12_BaseCheck.py)

### Approach

I created lists containing the digits `0`–`9` and letters `A`–`Z`. I then used a loop to build a dictionary of valid characters for every base from 2 through 36.

The function checks each character in the input after converting it to uppercase. If a character isn't allowed in the selected base, it returns `False`. If all characters are valid, it returns `True`.

### Why I Chose This Approach

I understood lists, dictionaries, loops, and membership checks, so I used them to represent the rules for each base.

Building the lookup table myself helped me understand how the valid digits change between number systems without relying on a technique I wasn't yet comfortable with.

## August 13 — Fibonacci Sequence

**Solution:** [`August-13_FibonacciSequence.py`](August-2025/August-13_FibonacciSequence.py)

### Approach

I copied the starting sequence into a new list and repeatedly added its last two numbers until the requested length was reached. I also handled requested lengths of zero and one separately.

The loop checks the current length of the result. If it is shorter than the requested length, the function adds the last two numbers together and appends the result.

### Why I Chose This Approach

I was comfortable working with lists, `while` loops, and `append()`. Rather than using recursion or a more complicated technique, I used the list itself to keep track of the sequence as it grew.

I used negative indexing because `[-1]` accesses the last item and `[-2]` accesses the second-to-last item. These positions automatically refer to the newest numbers as the list grows.

## August 13 — Space Jam

**Solution:** [`August-13_SPACEJAM.py`](August-2025/August-13_SPACEJAM.py)

### Approach

I used three string operations in sequence.

First, I removed spaces using `replace(" ", "")`. Then I converted the remaining text to uppercase using `upper()`. Finally, I used `"  ".join()` to insert two spaces between every character.

### Why I Chose This Approach

I chose this approach because it uses straightforward string methods that I understand and can combine easily.

Each operation handles one part of the problem, which makes the solution simple to read and debug. Rather than manually looping through every character and building the output, I used Python's built-in string methods.

## August 14 — Jbelmud Text

**Solution:** [`August-14_jbelmuText.py`](August-2025/August-14_jbelmuText.py)

### Approach

I split the input sentence into individual words using `split()` and created an empty list to store the processed words.

I then looped through each word. Words with two or fewer characters were added to the result unchanged because they don't have any letters between the first and last characters to sort.

For longer words, I separated the first letter, middle letters, and last letter using indexing and slicing. I sorted only the middle letters alphabetically, joined them back into a string, and combined all three parts. Each transformed word was added to the list.

Finally, I used `" ".join()` to combine the processed words into the final sentence.

### Why I Chose This Approach

I chose this approach because it breaks the problem into steps I already understand: splitting strings, looping through lists, indexing, slicing, sorting, and joining strings.

Keeping the first letter, middle section, and last letter in separate variables made it easier for me to see exactly which part of each word was being changed.

I also handled short words separately so that I wouldn't try to rearrange letters that don't exist.

## August 15 — Anagram Checker

**Solution:** [`August-15_AnagramChecker.py`](August-2025/August-15_AnagramChecker.py)

### Approach

I used `replace(" ", "")` to remove spaces from both strings and converted them to lowercase using `lower()` to make the comparison case-insensitive.

I then used `sorted()` to arrange the characters alphabetically and compared the sorted results. If they matched, the strings were anagrams.

### Why I Chose This Approach

I chose sorting because it provides a straightforward way to compare two strings regardless of the original order of their characters. Removing spaces and converting to lowercase ensures that whitespace and casing do not affect the comparison.

## August 17 — Targeted Sum

**Solution:** [`August-17_TargetedSum.py`](August-2025/August-17_TargetedSum.py)

### Approach

I used a dictionary called `seen` to store numbers that had already been checked along with their indexes.

For each number, I calculated the difference between the target and the current value. This tells me which number I need to find to reach the target.

If that difference already exists in the dictionary, I return the index of the previously stored number and the current index. Otherwise, I add the current value and its index to the dictionary.

### Why I Chose This Approach

I chose this approach because it avoids checking every possible pair of numbers. Once I understood why `target - value` finds the number needed to complete the sum, the dictionary approach made sense to me.

## August 18 — Factorializer

**Solution:** [`August-18_Factorializer.py`](August-2025/August-18_Factorializer.py)

### Approach

I created a range of numbers from `1` up to the given number and used a loop to multiply each number into a running total.

The total starts at `1` because multiplying by zero would make every result zero. This approach also naturally handles the factorial of zero.

### Why I Chose This Approach

I chose a loop because multiplication and running totals are concepts I already understood. It allowed me to see exactly how a factorial is built step by step.

## August 19 — Sum of Squares

**Solution:** [`August-19_SumSquares.py`](August-2025/August-19_SumSquares.py)

### Approach

I created a list containing the numbers from `1` up to the given number. I then used one loop to square each number and store the results in a new list.

After that, I used another loop to add all the squared values together.

### Why I Chose This Approach

I chose to separate the problem into two steps because it was easier for me to understand: first create the squares, then add them together.

Although the two steps could be combined, this approach made it easier to see what was happening at each stage.

## August 20 — 3 Strikes

**Solution:** [`August-20_3Strikes.py`](August-2025/August-20_3Strikes.py)

### Approach

I looped through every number from `1` up to the given number and calculated its square.

I then converted the square into a string and checked whether the digit `"3"` appeared anywhere in it. If it did, I increased the total count.

### Why I Chose This Approach

I chose this approach because it breaks the problem into simple steps that I understood: loop through the numbers, calculate the square, convert it to a string, and check for the digit.

## August 21 — Mile Pace

**Solution:** [`August-21_MilePace.py`](August-2025/August-21_MilePace.py)

### Approach

I split the duration string into minutes and seconds, then converted the entire duration into seconds.

I divided the total number of seconds by the number of miles to find the average time per mile. I then converted the result back into minutes and seconds.

Finally, I used an f-string with formatting to ensure that both minutes and seconds have leading zeros when necessary.

### Why I Chose This Approach

I chose to convert everything into seconds first because it made the calculation easier. Once I had the average number of seconds per mile, I could convert the result back into the required format.

## August 22 — Message Decoder

**Solution:** [`August-22_MessageDecoder.py`](August-2025/August-22_MessageDecoder.py)

### Approach

I looped through every character in the encoded message and checked whether it was a letter.

For letters, I checked whether they were uppercase or lowercase so the decoded character could keep the same case. I used `ord()` to convert characters into numerical positions and `chr()` to convert the decoded positions back into characters.

I reversed the original shift to decode each letter, while `% 26` handles wrapping around the alphabet. Non-alphabetical characters are added to the decoded message unchanged.

### Why I Chose This Approach

This challenge introduced me to a different way of working with characters by using their numerical values. I used this approach because it correctly handles uppercase letters, lowercase letters, wrapping around the alphabet, and non-letter characters.

## August 23 — Unnatural Prime

**Solution:** [`August-23_UnaturalPrime.py`](August-2025/August-23_UnaturalPrime.py)

### Approach

I converted the number into a string and removed a negative sign if one was present. This allowed me to check the positive version of the number, since a negative prime is simply the negative version of a positive prime.

I first checked whether the number was less than `2`, because `0` and `1` are not prime numbers.

I then looped through possible divisors from `2` up to the number. If any number divided evenly into it, I returned `False`. If no divisors were found, the number was prime.

### Why I Chose This Approach

I chose a loop because it helped me understand the definition of a prime number directly: a prime should not be evenly divisible by any number other than `1` and itself.

## August 25 — Camel Case

**Solution:** [`August-25_cameCase.py`](August-2025/August-25_cameCase.py)

### Approach

I first replaced dashes and underscores with spaces so that all word separators could be handled in the same way.

I then used `split()` to separate the text into individual words. The first word was converted to lowercase, while every following word was capitalized and added to the result.

### Why I Chose This Approach

I chose this approach because replacing all the separators with spaces simplified the problem. After that, I could use familiar string methods to process the words.

## Future Updates

I'll add new challenges to this README as I complete them, with a link to the Python file and a short explanation of my approach.

---

*More challenges coming soon.*
