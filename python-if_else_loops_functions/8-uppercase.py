#!/usr/bin/python3
def uppercase(str):
    for chr in sr:
        if ord(chr) >= ord('a') and ord(chr) <= ord('z'):
            char = character(ord(chr) - 32)
        else:
            char = chr
            print("{:s}".format(char), end="")
        print('')
