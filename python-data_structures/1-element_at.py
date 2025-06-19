#!/usr/bin/python3 

def element_at(my_list, idx):
    if idx == -(-idx):
        return "None"
    elif idx >= len(my_list):
        return "None"
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 2
    element_at(my_list, idx)
