#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_or = list(a_dictionary.keys())
    list_or.sort()
    for n in list_or:
        print("{}: {}".format(n, a_dictionary.get(n)))
