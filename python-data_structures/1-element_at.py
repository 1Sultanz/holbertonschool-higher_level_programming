#!/usr/bin/python3 

def element_at(my_list, idx):
    if idx != -(-idx):
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 5
    element_at(my_list, idx)
    print("Element at index {:d} is {}".format(idx, my_list[idx]))
