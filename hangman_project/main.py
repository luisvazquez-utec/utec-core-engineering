#!/usr/bin/env python3
"""Run the Hangman game from the command line."""

from game import HangmanGame
from utils import (
    format_guessed_letters,
    get_random_word,
    is_valid_guess,
)


def display_status(game):
    """Print the current word, guesses, and error count."""
    print("Word:")
    game.display_progress()
    print("Guessed letters: {}".format(
        format_guessed_letters(game.guessed_letters)
    ))
    print("Incorrect guesses: {}/{}".format(
        game.errors, game.max_errors
    ))


def main():
    """Run one interactive Hangman round."""
    game = HangmanGame(get_random_word())
    print("Welcome to Hangman!")

    while not game.is_over:
        guess = input("Guess a letter: ").strip().lower()
        if not is_valid_guess(guess):
            print("Enter a single letter.")
            continue

        result = game.guess(guess)
        if result is None:
            print("You already guessed that letter.")
        elif not result:
            print("That letter is not in the phrase.")
        display_status(game)

    if game.is_won:
        print("You win! The word was: {}".format(game.word))
    else:
        print("Game over! The word was: {}".format(game.word))


if __name__ == "__main__":
    main()
