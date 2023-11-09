#!/usr/bin/python3
# roman_to_int - returns a new dictionary with all values multiplied by two.
def roman_to_int(roman_string):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_value = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    for char in reversed(roman_string):
        val = roman_numerals.get(char, 0)
        if val >= prev_value:
            res += val
        else:
            res -= val
        prev_value = val
    return res
    
