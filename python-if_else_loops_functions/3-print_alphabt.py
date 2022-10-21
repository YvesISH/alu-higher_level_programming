#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if alphabet != ord('e') and alphabet != ord('q'):
        print("{:c}".format(alphabet), end="")
