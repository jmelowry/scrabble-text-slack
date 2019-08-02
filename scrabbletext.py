#!/usr/bin/env python

from sys import argv

def convert_string(string):
'''replaces individual letters and spaces w/ emoji representation'''

    modified = []
    for item in string:
        if item == " ":
            substring = ":scrabble_blank:"
        else:
            substring = ":scrabble_{0}:".format(item)

        modified.append(substring)

    rendered_string = "".join(modified)

    print(rendered_string)
    return rendered_string


if __name__ == "__main__":
    convert_string(argv[1])
