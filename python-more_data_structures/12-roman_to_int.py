#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for index, char in enumerate(roman_string):
        if index == len(roman_string) - 1:
            total += roman[char]
        elif roman[char] < roman[roman_string[index+1]]:
            total = total + (roman[roman_string[index+1]] - roman[char])
            pass
        else:
            total += roman[char]
    return total
