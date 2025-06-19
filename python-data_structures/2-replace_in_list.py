#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    element = 9
    new_list = []
    result = replace_in_list(my_list, idx, element) 
    if result != my_list:
        my_list[idx] = element
        new_list = my_list
        print(new_list)
    else:
        print(my_list)

