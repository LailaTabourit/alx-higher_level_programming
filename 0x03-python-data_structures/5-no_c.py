#!/usr/bin/python3
def no_c(my_string):
    leng = len(my_string)
    i = 0
    new_s = my_string[:]

    for j in range(leng):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            new_s = new_s[:(j - i)] + my_string[(j + 1):]
            i += 1
    return (new_s)
