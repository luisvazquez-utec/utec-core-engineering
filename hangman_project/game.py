#!/usr/bin/env python3
"""Define the state and rules for a Hangman game."""

from utils import is_valid_guess

MAX_ERRORS = 6


class HangmanGame:
    """Track guesses and determine whether a Hangman round has ended."""

    def __init__(self, phrase):
        """Initialize a round with a phrase containing at least one letter."""
        if not phrase or not any(character.isalpha() for character in phrase):
            raise ValueError("phrase must contain at least one letter")
        self.phrase = phrase
        self.guessed_letters = set()
        self.incorrect_guesses = 0

    def guess(self, letter):
        """Record a new letter; return correctness or None for a repeat."""
        if not is_valid_guess(letter):
            raise ValueError("guess must be a single letter")

        letter = letter.lower()
        if letter in self.guessed_letters:
            return None

        self.guessed_letters.add(letter)
        if letter not in self.phrase.lower():
            self.incorrect_guesses += 1
            return False
        return True

    @property
    def is_won(self):
        """Return whether every letter in the phrase has been guessed."""
        return all(
            not character.isalpha()
            or character.lower() in self.guessed_letters
            for character in self.phrase
        )

    @property
    def is_lost(self):
        """Return whether the maximum number of incorrect guesses is reached."""
        return self.incorrect_guesses >= MAX_ERRORS

    @property
    def is_over(self):
        """Return whether the player has won or lost."""
        return self.is_won or self.is_lost
