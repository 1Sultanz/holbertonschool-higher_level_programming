#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 1

    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 1

    return (a1 + b1, a2 + b2)

if __name__ == "__main__":
    print(add_tuple((1, 2), (3, 4)))
