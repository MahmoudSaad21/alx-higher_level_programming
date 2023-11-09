#!/usr/bin/python3
def roman_to_int(roman_string):
  sum = 0
  for i in roman_string:
    if i == 'I':
      sum = sum + 1
    elif i == 'V':
      sum = sum + 5
    elif i == 'X':
      sum = sum + 10
    elif i == 'L':
      sum = sum + 50
    elif i == 'C':
      sum = sum + 100
    elif i == 'D':
      sum = sum + 500
    elif i == 'M':
      sum = sum + 1000
  return sum
