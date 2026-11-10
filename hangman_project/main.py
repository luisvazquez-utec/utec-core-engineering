#!/usr/bin/env python3
"""Ejecuta el juego del ahorcado desde la línea de comandos."""

from game import HangmanGame
from utils import (
    format_guessed_letters,
    get_random_word,
    is_valid_guess,
)


def display_status(game):
    """Muestra la palabra, las letras intentadas y los intentos restantes."""
    print("Palabra:")
    game.display_progress()
    print("Letras intentadas: {}".format(
        format_guessed_letters(game.guessed_letters)
    ))
    print("Intentos restantes: {}".format(game.max_errors - game.errors))


def main():
    """Ejecuta una ronda interactiva del ahorcado."""
    game = HangmanGame(get_random_word())
    print("¡Bienvenido al ahorcado!")

    while not game.is_over:
        guess = input("Adivina una letra: ").lower()
        if not is_valid_guess(guess):
            print("Ingresa una sola letra.")
            continue

        if guess in game.guessed_letters:
            print("Ya intentaste esa letra.")
            continue

        if not game.process_guess(guess):
            print("La palabra no contiene esa letra.")
        display_status(game)

    if game.is_won():
        print("¡Ganaste! La palabra era: {}".format(game.word))
    else:
        print("Fin del juego. La palabra era: {}".format(game.word))


if __name__ == "__main__":
    main()
