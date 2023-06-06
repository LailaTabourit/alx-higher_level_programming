#!/usr/bin/python3
for h in reversed(range(97, 123)):
    print("{:c}".format(h if (h % 2 == 0) else (h - 32)), end='')
