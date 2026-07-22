#!/usr/bin/python3
"""Module that prints text with extra newlines after ., ? and :.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ., ? and : character.

    Args:
        text (str): the text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
