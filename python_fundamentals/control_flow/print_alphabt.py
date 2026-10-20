#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""
for letter in alphabet:
    if letter != "q" and letter != "e":
        result += letter
print("{}".format(result), end="")
