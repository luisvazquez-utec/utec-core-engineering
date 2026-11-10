# Hangman

A console-based Hangman game. The game selects an alphabetic word from
`wordlist.txt`; guess its letters before making six incorrect guesses.

## Run

From this directory, start the game with:

```sh
python3 main.py
```

## Modules

- `main.py` runs the interactive game loop.
- `game.py` implements the `HangmanGame` state and rules.
- `utils.py` selects a random word, validates guesses, and formats the display.
- `wordlist.txt` contains one alphabetic candidate word per line.
