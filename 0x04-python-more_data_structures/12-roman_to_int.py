#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    sum = 0
    k = 0
    if isinstance(roman_string, str):
        while k < len(roman_string):
            if k + 1 < len(roman_string) and roman_string[k: k+2] in roman:
                sum += roman.get(roman_string[k: k+2])
                k += 2
            else:
                sum += roman.get(roman_string[k])
                k += 1
    return (sum)
