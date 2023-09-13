#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string == None:
        return 0
    dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    number = dic[roman_string[0]]
    for i in range(1, len(roman_string)):
        number = number + dic[roman_string[i]]
        if dic[roman_string[i]] > dic[roman_string[i - 1]]:
            number = number - 2 * dic[roman_string[i - 1]]
    return number
