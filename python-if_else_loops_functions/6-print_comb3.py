#!/usr/bin/python3
for number in range(0, 9):
    for numbers in range(number + 1, 10):
        if number == 8:
            print("{}{}".format(number, numbers))
        else:
            print("{}{}".format(number, numbers), end=", ")
