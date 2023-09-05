#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        temp = str
    else:
        temp = str[0:n] + str[n + 1:]
    return temp
