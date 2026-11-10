#!/usr/bin/env python3
"""Define the state and rules for a Hangman game."""

from utils import is_valid_guess

MAX_ERRORS = 6


class HangmanGame:
    """Track guesses and determine whether a Hangman round has ended."""

    def __init__(self, word):
        """Initialize a round with a word containing at least one letter."""
        if not word or not any(character.isalpha() for character in word):
            raise ValueError("word must contain at least one letter")
        self.word = word
        self.guessed_letters = []
        self.max_errors = MAX_ERRORS
        self.errors = 0

    def display_progress(self):
        """Print guessed letters in place and hide the remaining letters."""
        progress = []
        for character in self.word:
            if not character.isalpha():
                progress.append(character)
            elif character.lower() in self.guessed_letters:
                progress.append(character)
            else:
                progress.append("_")
        print(" ".join(progress))

    def process_guess(self, letter):
        """Record a letter and return whether it occurs in the word."""
        if not is_valid_guess(letter):
            raise ValueError("guess must be a single letter")

        letter = letter.lower()
        if letter in self.guessed_letters:
            return letter in self.word.lower()

        self.guessed_letters.append(letter)
        if letter not in self.word.lower():
            self.errors += 1
            return False
        return True

    def guess(self, letter):
        """Record a new guess, preserving None as the result for repeats."""
        normalized_letter = letter.lower() if isinstance(letter, str) else letter
        if normalized_letter in self.guessed_letters:
            return None
        return self.process_guess(letter)

    def is_won(self):
        """Return whether every letter in the word has been guessed."""
        return all(
            not character.isalpha()
            or character.lower() in self.guessed_letters
            for character in self.word
        )

    def is_lost(self):
        """Return whether the maximum number of incorrect guesses is reached."""
        return self.errors >= self.max_errors

    @property
    def is_over(self):
        """Return whether the player has won or lost."""
        return self.is_won() or self.is_lost()
