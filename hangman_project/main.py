#!/usr/bin/env python3
"""Run the Hangman game from the command line."""

from game import HangmanGame, MAX_ERRORS
from utils import (
    display_word,
    format_guessed_letters,
    get_random_word,
    is_valid_guess,
)


def display_status(game):
    """Print the current phrase, guesses, and remaining error allowance."""
    print("Phrase: {}".format(display_word(
        game.phrase, game.guessed_letters
    )))
    print("Guessed letters: {}".format(
        format_guessed_letters(game.guessed_letters)
    ))
    print("Incorrect guesses: {}/{}".format(
        game.incorrect_guesses, MAX_ERRORS
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
        print("You win! The phrase was: {}".format(game.phrase))
    else:
        print("Game over! The phrase was: {}".format(game.phrase))


if __name__ == "__main__":
    main()
