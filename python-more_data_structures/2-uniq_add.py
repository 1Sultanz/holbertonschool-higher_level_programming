#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    unique = set(my_list)
    for n in unique:
        total += n
    return total

    if __name__ == "__main__":
        my_list = [1, 2, 3, 1, 4, 2, 5]
        result = uniq_add(my_list)
        print("Result: {:d}".format(result))
