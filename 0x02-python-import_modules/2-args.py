#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    m = 1
    argc = len(sys.argv) - m
    print('{} argument{}{}'.format(
        argc, 's' * (argc != 1),
        ':' if argc > 0 else '.'
        ))
    for arg in sys.argv[m:]:
        print('{}: {}'.format(m, arg))
        m += 1
