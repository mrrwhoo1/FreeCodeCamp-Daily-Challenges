# freeCodeCamp Daily Coding Challenges

My Python solutions to freeCodeCamp's Daily Coding Challenges. I use this repository to keep track of the challenges I've completed and how I approached each one.

## Repository Structure

<details>
<summary>Click to view the repository structure</summary>

<br />

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
    ├── August-25_cameCase.py
    ├── August-27_UnorderOfOperations.py
    ├── August-28_SecondBest.py
    ├── August-29_CandleLight.py
    └── August-30_ArrayDuplicates.py
```

</details>

## Table of Contents

- [About This Repository](#about-this-repository)
- [My Problem-Solving Philosophy](#my-problem-solving-philosophy)
- [Progress](#progress)
- [August 11 — Vowel Balance](#august-11--vowel-balance)
- [August 12 — Base Check](#august-12--base-check)
- [August 13 — Fibonacci Sequence](#august-13--fibonacci-sequence)
- [August 14 — Space Jam](#august-14--space-jam)
- [August 15 — Jbelmud Text](#august-15--jbelmud-text)
- [August 16 — Anagram Checker](#august-16--anagram-checker)
- [August 17 — Targeted Sum](#august-17--targeted-sum)
- [August 18 — Factorializer](#august-18--factorializer)
- [August 19 — Sum of Squares](#august-19--sum-of-squares)
- [August 20 — 3 Strikes](#august-20--3-strikes)
- [August 21 — Mile Pace](#august-21--mile-pace)
- [August 22 — Message Decoder](#august-22--message-decoder)
- [August 23 — Unnatural Prime](#august-23--unnatural-prime)
- [August 24 — Character Battle](#august-24--character-battle)
- [August 25 — Camel Case](#august-25--camel-case)
- [August 27 — Unorder of Operations](#august-27--unorder-of-operations)
- [August 28 — Second Best](#august-28--second-best)
- [August 29 — Candlelight](#august-29--candlelight)
- [August 30 — Array Duplicates](#august-30--array-duplicates)

## About This Repository

This repository contains my Python solutions to the daily challenges. I focus on writing code I understand and can explain, rather than choosing a complicated approach just because it is shorter or more advanced.

Each entry briefly describes how I approached the problem and why I chose that approach.

## My Problem-Solving Philosophy

I try to understand the problem first, then solve it using Python features I know how to use. My solutions may not always be the most efficient, but I want them to be readable and make sense to me. As I get more practice, I can revisit older solutions and improve them.

## Progress

- **Challenges completed:** 19
- **Challenge period:** August 2025
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

## August 12 — Base Check

**Solution:** [`August-12_BaseCheck.py`](August-2025/August-12_BaseCheck.py)

### Approach

I created lists containing the digits `0`–`9` and letters `A`–`Z`. I then used a loop to build a dictionary of valid characters for every base from 2 through 36.

The function checks each character in the input after converting it to uppercase. If a character isn't allowed in the selected base, it returns `False`. If all characters are valid, it returns `True`.

### Why I Chose This Approach

I understood lists, dictionaries, loops, and membership checks, so I used them to represent the rules for each base. Building the lookup table myself helped me understand how the valid digits change between number systems.

## August 13 — Fibonacci Sequence

**Solution:** [`August-13_FibonacciSequence.py`](August-2025/August-13_FibonacciSequence.py)

### Approach

I copied the starting sequence into a new list and repeatedly added its last two numbers until the requested length was reached. I also handled requested lengths of zero and one separately.

### Why I Chose This Approach

I was comfortable working with lists, `while` loops, and `append()`. Rather than using recursion, I used the list itself to keep track of the sequence as it grew. Negative indexing let me access the latest two values.

## August 14 — Space Jam

**Solution:** [`August-14_SPACEJAM.py`](August-2025/August-14_SPACEJAM.py)

### Approach

I removed normal spaces from the text, converted the remaining characters to uppercase, and used `"  ".join()` to insert two spaces between every character.

### Why I Chose This Approach

I chose this approach because it uses straightforward string methods that I understand. Each operation handles one part of the problem, making the solution easy to follow.

## August 15 — Jbelmud Text

**Solution:** [`August-15_jbelmuText.py`](August-2025/August-15_jbelmuText.py)

### Approach

I split the sentence into words and looped through them. For each word, I kept the first and last characters in place, sorted the characters in between, and joined the parts back together. Short words were left unchanged.

### Why I Chose This Approach

This approach uses string splitting, loops, indexing, slicing, sorting, and joining. Keeping the first, middle, and last parts separate made it easier to see which characters were being rearranged.

## August 16 — Anagram Checker

**Solution:** [`August-16_AnagramChecker.py`](August-2025/August-16_AnagramChecker.py)

### Approach

I removed normal spaces from both strings using `replace(" ", "")` and converted them to lowercase. I then used `sorted()` to arrange the characters alphabetically and compared the results.

### Why I Chose This Approach

Sorting provides a straightforward way to compare strings regardless of the original order of their characters. Converting to lowercase makes the comparison case-insensitive.

## August 17 — Targeted Sum

**Solution:** [`August-17_TargetedSum.py`](August-2025/August-17_TargetedSum.py)

### Approach

I used a dictionary called `seen` to store numbers that had already been checked along with their indexes.

For each number, I calculated the difference between the target and the current value. This tells me which number I need to find to reach the target. If that difference is already in the dictionary, I return the stored index and the current index. Otherwise, I store the current number and its index.

### Why I Chose This Approach

I chose this approach because it avoids checking every possible pair of numbers. Once I understood why `target - value` finds the number needed to complete the sum, the dictionary approach made sense to me.

## August 18 — Factorializer

**Solution:** [`August-18_Factorializer.py`](August-2025/August-18_Factorializer.py)

### Approach

I used a loop to multiply each number from `1` up to the given number into a running total. The total starts at `1`, which also allows the factorial of zero to be handled correctly.

### Why I Chose This Approach

A running total and a loop were concepts I already understood. This let me see how the factorial is built one multiplication at a time.

## August 19 — Sum of Squares

**Solution:** [`August-19_SumSquares.py`](August-2025/August-19_SumSquares.py)

### Approach

I created a list of numbers, used a loop to square each number and store the results in another list, then used a separate loop to add the squared values together.

### Why I Chose This Approach

I separated the problem into two steps because it was easier for me to follow: first create the squares, then calculate their sum.

## August 20 — 3 Strikes

**Solution:** [`August-20_3Strikes.py`](August-2025/August-20_3Strikes.py)

### Approach

I looped through the numbers from `1` up to the given number and calculated each square. I converted each square to a string and checked whether the digit `"3"` appeared in it. If it did, I increased the count.

### Why I Chose This Approach

Converting the square to a string made it possible to check for a particular digit using a simple membership test. The loop keeps the process straightforward.

## August 21 — Mile Pace

**Solution:** [`August-21_MilePace.py`](August-2025/August-21_MilePace.py)

### Approach

I split the duration into minutes and seconds, then converted the time into total seconds. I divided that value by the number of miles to calculate the average time per mile, converted the result back into minutes and seconds, and formatted the output with leading zeros where needed.

### Why I Chose This Approach

Converting the time to seconds first made the calculation easier. I only had to convert it back to the required time format after finding the pace.

## August 22 — Message Decoder

**Solution:** [`August-22_MessageDecoder.py`](August-2025/August-22_MessageDecoder.py)

### Approach

I looped through each character and checked whether it was a letter. For letters, I used `ord()` to get the character's numerical position and `chr()` to convert the decoded position back into a character.

I handled uppercase and lowercase letters separately so the original case was preserved. I used modulo `26` to handle wrapping around the alphabet. Non-letter characters were kept unchanged.

### Why I Chose This Approach

Using character codes gave me a way to shift letters mathematically while preserving their case. Modulo made it possible to wrap around the alphabet without needing separate cases for the beginning and end.

## August 23 — Unnatural Prime

**Solution:** [`August-23_UnaturalPrime.py`](August-2025/August-23_UnaturalPrime.py)

### Approach

I handled negative values by working with the positive version of the number. I first checked whether the number was less than `2`, since those values are not prime.

I then looped through possible divisors. If any value divided evenly into the number, the function returned `False`. If no divisor was found, it returned `True`.

### Why I Chose This Approach

I used a loop to check the definition of a prime number directly: it should not be evenly divisible by any number other than `1` and itself.

## August 24 — Character Battle

**Solution:** [`August-24_CharacterBattle.py`](August-2025/August-24_CharacterBattle.py)

### Approach

I created a dictionary that assigns strengths to lowercase letters, uppercase letters, and digits. Characters that are not in the dictionary are treated as having a strength of zero.

I used `zip()` to pair each character in my army with the character at the same position in the opposing army. I compared their strengths and counted how many individual battles each side won.

Before comparing the battle results, I checked the lengths of both armies to handle the retreat conditions.

### Why I Chose This Approach

The dictionary keeps the character strengths in one place, while `get()` lets me provide a default strength for characters that are not listed. Using `zip()` made it easy to compare matching positions without manually managing two indexes.

## August 25 — Camel Case

**Solution:** [`August-25_cameCase.py`](August-2025/August-25_cameCase.py)

### Approach

I replaced dashes and underscores with spaces so that both separators could be handled in the same way. I then split the text into words, converted the first word to lowercase, and capitalized each following word before joining everything together.

### Why I Chose This Approach

Replacing the separators first simplified the problem. After that, I could use string methods I was already familiar with to build the camel-case result.

## August 27 — Unorder of Operations

**Solution:** [`August-27_UnorderOfOperations.py`](August-2025/August-27_UnorderOfOperations.py)

### Approach

I started with the first number as the running total, then processed the remaining numbers from left to right. I applied the next operator to the running total and current number, moving through the operator list in order. When I reached the end of the operator list, I reset the operator index to the beginning.

The operations are applied in sequence rather than using normal mathematical operator precedence. Division uses floor division (`//`).

### Why I Chose This Approach

Using a running total let me perform one operation at a time and keep track of the result. An index made it possible to cycle through the operators without needing a more complicated expression evaluator.

## August 28 — Second Best

**Solution:** [`August-28_SecondBest.py`](August-2025/August-28_SecondBest.py)

### Approach

I used `set()` to remove duplicate laptop prices and `sorted()` to arrange the remaining prices. I then selected the second-highest distinct price.

If that price was over the budget, I checked the available prices and returned the highest one that was still affordable. If no price was affordable, the function returned `0`.

### Why I Chose This Approach

Removing duplicates before sorting made it easier to identify the second-highest distinct price. Sorting also gave me a clear order to use when checking the budget.

## August 29 — Candlelight

**Solution:** [`August-29_CandleLight.py`](August-2025/August-29_CandleLight.py)

### Approach

I kept two running totals: `total_burned` for every candle I've burned so far, and `leftovers` for the burned candles waiting to be recycled. In each round of a `while` loop, I burned all the candles I had, adding them to both totals.

I then used floor division (`//`) to work out how many new candles the leftovers could make, and modulo (`%`) to keep whatever was left over for the next round. The loop stops once there are no candles left to burn.

### Why I Chose This Approach

Simulating the process round by round matched the way the problem is described, so it was easy for me to follow. `//` and `%` split the leftovers into "new candles" and "still waiting" cleanly, without needing any extra data structures.

## August 30 — Array Duplicates

**Solution:** [`August-30_ArrayDuplicates.py`](August-2025/August-30_ArrayDuplicates.py)

### Approach

I used a set to get the unique values in the array. I then checked how many times each value appeared in the original array using `count()`. Values that appeared more than once were added to the duplicates list, which I sorted before returning.

### Why I Chose This Approach

Using a set gave me a simple way to avoid checking the same value repeatedly. I used `count()` to check whether each unique value appeared more than once, then sorted the result to return it in order.

---

I'll keep adding new challenges here as I complete them.
