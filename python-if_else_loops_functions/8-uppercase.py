#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) >= ord('a') and ord(character) <= ord('z'):
            char = chr(ord(character) - 32)
        else:
            char = character
        print("{:s}".format(char), end="")
    print('')
