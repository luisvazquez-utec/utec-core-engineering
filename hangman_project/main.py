#!/usr/bin/env python3
"""Run the Hangman game from the command line."""

from game import HangmanGame
from utils import (
    format_guessed_letters,
    get_random_word,
    is_valid_guess,
)


def display_status(game):
    """Print the current word, guessed letters, and remaining attempts."""
    print("Word:")
    game.display_progress()
    print("Guessed letters: {}".format(
        format_guessed_letters(game.guessed_letters)
    ))
    print("Attempts remaining: {}".format(game.max_errors - game.errors))


def main():
    """Run one interactive Hangman round."""
    game = HangmanGame(get_random_word())
    print("Welcome to Hangman!")

    while not game.is_over:
        guess = input("Guess a letter: ").lower()
        if not is_valid_guess(guess):
            print("Enter a single letter.")
            continue

        if guess in game.guessed_letters:
            print("You already guessed that letter.")
            continue

        if not game.process_guess(guess):
            print("That letter is not in the phrase.")
        display_status(game)

    if game.is_won():
        print("¡Ganaste! La palabra era: {}".format(game.word))
    else:
        print("Fin del juego. La palabra era: {}".format(game.word))


if __name__ == "__main__":
    main()
