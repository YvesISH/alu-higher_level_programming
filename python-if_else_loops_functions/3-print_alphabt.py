#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if n != ord('e') and n != ord('q'):
        print("{:c}".format(n), end="")
