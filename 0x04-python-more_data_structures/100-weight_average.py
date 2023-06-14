#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    nm = 0
    dn = 0

    for tp in my_list:
        nm += tp[0] * tp[1]
        dn += tp[1]
    return (nm / dn)
