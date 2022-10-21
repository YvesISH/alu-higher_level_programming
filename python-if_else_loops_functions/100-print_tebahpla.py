#!/usr/bin/python3
for lt in range(122, 96, -1):
    if lt % 2 != 0:
        lt -= 32
    print("{}".format(chr(lt)), end="")
