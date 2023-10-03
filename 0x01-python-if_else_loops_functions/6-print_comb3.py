#!/usr/bin/python3
for num in range(89):
    if num % 10 > num // 10:
        print("{0:02d}".format(num), end=", ")
print("{0}".format(89))
