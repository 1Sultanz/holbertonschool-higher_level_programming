#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict


def print_sorted_dictionary(a_dictionary):
    for key in a_dictionary:
        print(f"{key} : {a_dictionary[key]}")


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
