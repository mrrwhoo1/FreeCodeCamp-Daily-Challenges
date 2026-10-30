# FreeCodeCamp Daily Coding Challenges

My Python solutions to freeCodeCamp's Daily Coding Challenges. This repository documents my progress, problem-solving approaches, and what I learn from each challenge.

## Repository Structure

```text
FreeCodeCamp-Daily-Challenges/
├── README.md
└── August-2025/
    ├── August-11_VowelBalance.py
    ├── August-12_BaseCheck.py
    ├── August-13_FibonacciSequence.py
```

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
| [Future Updates](#future-updates) | — | — |

## About This Repository

I'm using these challenges to improve my Python skills and become a better problem solver.

My approach is to **solve problems using methods I understand and can confidently implement**. I don't always choose the fastest or most advanced solution. I'd rather write a solution I can explain, understand why it works, and gradually learn better approaches as my skills improve.

For each challenge, I document:

- **My approach:** How I broke down the problem.
- **Why I chose it:** Why the method made sense to me at the time.
- **How it works:** The important parts of my solution.
- **What I learned:** Anything I discovered or could improve.

## My Problem-Solving Philosophy

I want this repository to show more than whether my code works. I want it to show how my thinking develops over time.

1. **Understand the problem** before writing code.
2. **Write solutions I can explain** rather than using techniques I don't understand.
3. **Break problems into manageable steps** using familiar Python features where possible.
4. **Learn from each challenge**, including mistakes and alternative approaches.
5. **Improve gradually** as I become more confident with Python and problem-solving.

An approach doesn't have to be the most efficient one to be a useful learning step. Once I understand my original solution, I can explore ways to make it simpler, more reusable, or more efficient.

## Progress

- **Challenges completed:** 5
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

### What I Learned

- How to split strings using slicing.
- How to handle odd and even string lengths.
- How to count specific characters and compare totals.

## August 12 — Base Check

**Solution:** [`August-12_BaseCheck.py`](August-2025/August-12_BaseCheck.py)

### Approach

I created lists containing the digits `0`–`9` and letters `A`–`Z`. I then used a loop to build a dictionary of valid characters for every base from 2 through 36.

The function checks each character in the input after converting it to uppercase. If a character isn't allowed in the selected base, it returns `False`. If all characters are valid, it returns `True`.

### Why I Chose This Approach

I understood lists, dictionaries, loops, and membership checks, so I used them to represent the rules for each base.

Building the lookup table myself helped me understand how the valid digits change between number systems without relying on a technique I wasn't yet comfortable with.

### What I Learned

- How number bases determine which digits are allowed.
- How to generate dictionary entries using loops.
- How to validate input character by character.
- How converting characters to uppercase simplifies case handling.

## August 13 — Fibonacci Sequence

**Solution:** [`August-13_FibonacciSequence.py`](August-2025/August-13_FibonacciSequence.py)

### Approach

I copied the starting sequence into a new list and repeatedly added its last two numbers until the requested length was reached. I also handled requested lengths of zero and one separately.

The loop checks the current length of the result. If it is shorter than the requested length, the function adds the last two numbers together and appends the result.

### Why I Chose This Approach

I was comfortable working with lists, `while` loops, and `append()`. Rather than using recursion or a more complicated technique, I used the list itself to keep track of the sequence as it grew.

I used negative indexing because `[-1]` accesses the last item and `[-2]` accesses the second-to-last item. These positions automatically refer to the newest numbers as the list grows.

### What I Learned

- How to build a list dynamically.
- How to use negative indexing to access recent values.
- How a `while` loop can continue until a changing condition is met.
- Why the list's current length matters when generating a sequence of a specific size.

## August 13 — Space Jam

**Solution:** [`August-13_SPACEJAM.py`](August-2025/August-13_SPACEJAM.py)

### Approach

I used three string operations in sequence.

First, I removed spaces using `replace(" ", "")`. Then I converted the remaining text to uppercase using `upper()`. Finally, I used `"  ".join()` to insert two spaces between every character.

### Why I Chose This Approach

I chose this approach because it uses straightforward string methods that I understand and can combine easily.

Each operation handles one part of the problem, which makes the solution simple to read and debug. Rather than manually looping through every character and building the output, I used Python's built-in string methods.

### What I Learned

- How to remove spaces using `replace()`.
- How to convert a string to uppercase using `upper()`.
- How `join()` inserts a separator between every item in an iterable.
- That `join()` can be used directly on a string because strings are iterable.

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

### What I Learned

- How `split()` separates a sentence into words.
- How to use `word[0]`, `word[1:-1]`, and `word[-1]` to access different parts of a word.
- How `sorted()` arranges characters alphabetically and returns a list.


## August 15 – Anagram Checker
**Solution:** [`August-15_AnagramChecker.py`](August-2025/August-15_AnagramChecker.py)

## Approach:
- Used .replace(" ", "") to remove spaces from both strings.
- Converted both strings to lowercase using .lower() to make the comparison case-insensitive.
- Used sorted() to arrange the characters alphabetically.
- Compared the sorted results. If they matched, the strings were anagrams; otherwise, they were not.

## Why I chose this approach:

I chose sorting because it provides a straightforward way to compare two strings regardless of the original order of their characters. Removing spaces and converting to lowercase ensures that whitespace and casing do not affect the comparison.

## What I learned:

This challenge reinforced my understanding of string manipulation and sorting. I applied methods I had already encountered in previous challenges, combining them to solve a new problem.
---



## Future Updates

This README will be updated as I complete more challenges. Each new challenge will get:

- An entry in the table of contents.
- A link to its Python solution.
- An explanation of my approach and why I chose it.
- A summary of what I learned and what I could improve.

---

*Learning Python one challenge at a time.*
