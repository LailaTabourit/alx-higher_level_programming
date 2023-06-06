#!/usr/bin/python3
for n in range(97, 123):
    if chr(n) not in ['e', 'q']:
        print("{}".format(chr(n)), end="")
