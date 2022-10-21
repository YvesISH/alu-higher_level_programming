#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print(number)
    else:
        print("{:0>2d}".format(number), end=", ")
