#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the alphabet(s) all in lowercase and do not let it be followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")

