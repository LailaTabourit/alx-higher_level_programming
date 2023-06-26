#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cmp = 0
    try:
        for i in range(x):
            print(my_list[i], end ="")
            cmp += 1
        print()
        return (cmp)
    except IndexError:
        print()
        return (cmp)
