#!/usr/bin/env python3
"""Proporciona selección de palabras y utilidades para el ahorcado."""

import random
from pathlib import Path


def get_random_word():
    """Devuelve una palabra alfabética aleatoria de wordlist.txt."""
    wordlist_path = Path(__file__).with_name("wordlist.txt")
    words = [
        line.strip()
        for line in wordlist_path.read_text(encoding="utf-8").splitlines()
        if line.strip().isalpha()
    ]
    if not words:
        raise ValueError(
            "wordlist.txt debe contener al menos una palabra alfabética"
        )
    return random.choice(words)


def is_valid_guess(guess):
    """Indica si la entrada contiene exactamente una letra."""
    return len(guess) == 1 and guess.isalpha()


def display_word(phrase, guessed_letters):
    """Oculta letras pendientes y revela espacios y signos de puntuación."""
    return "".join(
        character
        if not character.isalpha()
        or character.lower() in guessed_letters
        else "_"
        for character in phrase
    )


def format_guessed_letters(guessed_letters):
    """Devuelve las letras intentadas en un orden legible y consistente."""
    return ", ".join(sorted(guessed_letters)) or "ninguna"
