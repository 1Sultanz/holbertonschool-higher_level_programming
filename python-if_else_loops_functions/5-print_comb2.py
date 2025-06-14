#!/usr/bin/python3
i = 0
while i <= 99:
    if i < 99:
        print("{:02}".format(i), end=", ")
    else:
        print("{:02}".format(i))
    i += 1
