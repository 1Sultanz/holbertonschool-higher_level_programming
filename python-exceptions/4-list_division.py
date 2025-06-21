#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    try:
        i = 0
        while i < list_length:
            try:
                new.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                new.append(0)
                print("division by 0")
            except TypeError:
                new.append(0)
                print("wrong type")
            except IndexError:
                new.append(0)
                print("out of range")
            i += 1
    finally:
        return new


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
