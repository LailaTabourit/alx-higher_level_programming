#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    leng = len(my_list)

    if idx > leng - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
