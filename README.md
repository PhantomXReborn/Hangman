# Python Hangman Game

## Description
This is a simple Hangman game written in Python that runs in the terminal. The program randomly selects a word, and the player attempts to guess it one letter at a time. Correct guesses reveal the letters in the word, while incorrect guesses reduce the number of remaining attempts. The game ends when the player successfully guesses the word or runs out of attempts.

## Features
- Random word selection
- Letter-by-letter guessing
- Tracks incorrect guesses
- Displays current progress of the word
- Simple terminal-based interface

## Requirements
- Python 3.x

## How to Run
1. Download or clone this repository.
2. Navigate to the project folder in your terminal.
3. Run the program using:

```bash
python hangman.py
How to Play

The game will display blank spaces representing the hidden word.

Enter one letter at a time to guess the word.

If the letter is correct, it will appear in the correct position(s).

If the letter is incorrect, you will lose one attempt.

Continue guessing until you reveal the entire word or run out of attempts.

Example
Word: _ _ _ _ _
Guess a letter: a
Correct!

Word: _ a _ _ _
Guess a letter: z
Incorrect! Attempts remaining: 5
Author

Created as a beginner Python project to practice programming fundamentals such as loops, conditionals, and string handling.
