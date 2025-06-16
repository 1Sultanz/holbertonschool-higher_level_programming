#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument_count = len(sys.argv) - 1

if argument_count == 0:
    print("0 arguments.")
elif argument_count == 1:
    print("1 arguments:")
else:
    print("{} arguments:".format(argument_count))

i = 1
while i < len(sys.argv):
    print("{}: {}".format(i, sys.argv[i]))
    i += 1
