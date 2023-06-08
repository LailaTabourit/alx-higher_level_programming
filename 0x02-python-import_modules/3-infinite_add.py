#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    if (len(sys.argv) > 1):
        for n in range(1, len(sys.argv)):
            result += (int(sys.argv[n]))
    print("{:d}".format(result))
