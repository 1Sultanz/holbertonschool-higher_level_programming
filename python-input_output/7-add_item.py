#!/usr/bin/python3
"""Load, add, save"""

if __name__ == "__main__":
    import sys
    from save_to_json_file import save_to_json_file
    from load_from_json_file import load_from_json_file

    filename = "add_item.json"


    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)
