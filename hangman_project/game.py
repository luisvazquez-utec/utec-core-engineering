#!/usr/bin/env python3
"""Define el estado y las reglas de una partida de ahorcado."""

from utils import is_valid_guess

MAX_ERRORS = 6


class HangmanGame:
    """Registra las adivinanzas y determina cuándo termina la partida."""

    def __init__(self, word):
        """Inicia una partida con una palabra que contenga alguna letra."""
        if not word or not any(character.isalpha() for character in word):
            raise ValueError("la palabra debe contener al menos una letra")
        self.word = word
        self.guessed_letters = []
        self.max_errors = MAX_ERRORS
        self.errors = 0

    def display_progress(self):
        """Muestra las letras acertadas y oculta las que faltan."""
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
        """Registra una letra e indica si aparece en la palabra."""
        if not is_valid_guess(letter):
            raise ValueError("la adivinanza debe ser una sola letra")

        letter = letter.lower()
        if letter in self.guessed_letters:
            return letter in self.word.lower()

        self.guessed_letters.append(letter)
        if letter not in self.word.lower():
            self.errors += 1
            return False
        return True

    def guess(self, letter):
        """Registra una letra nueva y devuelve None si ya fue intentada."""
        normalized_letter = letter.lower() if isinstance(letter, str) else letter
        if normalized_letter in self.guessed_letters:
            return None
        return self.process_guess(letter)

    def is_won(self):
        """Indica si ya se adivinaron todas las letras de la palabra."""
        return all(
            not character.isalpha()
            or character.lower() in self.guessed_letters
            for character in self.word
        )

    def is_lost(self):
        """Indica si se alcanzó el máximo de errores permitidos."""
        return self.errors >= self.max_errors

    @property
    def is_over(self):
        """Indica si la partida terminó por victoria o derrota."""
        return self.is_won() or self.is_lost()
