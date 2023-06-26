#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        res = None

    return (res)
