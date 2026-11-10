#!/usr/bin/env python3
"""Provide input validation and display helpers for Hangman."""

import random
from pathlib import Path


def get_random_word():
    """Return a random alphabetic word from wordlist.txt."""
    wordlist_path = Path(__file__).with_name("wordlist.txt")
    words = [
        line.strip()
        for line in wordlist_path.read_text(encoding="utf-8").splitlines()
        if line.strip().isalpha()
    ]
    if not words:
        raise ValueError("wordlist.txt must contain at least one alphabetic word")
    return random.choice(words)


def is_valid_guess(guess):
    """Return whether guess is exactly one alphabetic character."""
    return len(guess) == 1 and guess.isalpha()


def display_word(phrase, guessed_letters):
    """Hide unguessed letters while revealing spaces and punctuation."""
    return "".join(
        character
        if not character.isalpha()
        or character.lower() in guessed_letters
        else "_"
        for character in phrase
    )


def format_guessed_letters(guessed_letters):
    """Return guessed letters in a consistent, readable order."""
    return ", ".join(sorted(guessed_letters)) or "none"
