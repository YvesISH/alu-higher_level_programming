#!/usr/bin/python3
def remove_char_at(str, n):
    pst = 0
    new = ""
    for char in str:
        if pst != n:
            new += char
        pst += 1
    return (new)
