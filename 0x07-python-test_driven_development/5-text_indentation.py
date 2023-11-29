#!/usr/bin/python3
"""2 newlines after each ['.', '?', ':']"""


def text_indentation(text):
    """ prints "text" with 2 newlines after each of these char: ['.', '?', ':']"""
    if type(text) != str:
        raise TypeError("text must be a string")
    af = ['.', '?', ':']

    # Removes the space after special chars
    idx = 0
    for items in text:
        if items in af:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    idx = 0
    for items in text:
        if items in af:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1

    print(text, end='')
