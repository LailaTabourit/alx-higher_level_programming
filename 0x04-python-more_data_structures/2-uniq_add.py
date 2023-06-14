#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_l = set(my_list)
    n = 0
    for i in uniq_l:
        n += i
    return (n)
