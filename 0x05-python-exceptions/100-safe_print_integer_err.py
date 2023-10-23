#!/usr/bin/python3
from sys import exc_info, stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        printed_correctly = True
    except (TypeError, ValueError):
        print("Exception: {}".format(exc_info()[1]), file=sys.stderr)
        printed_correctly = False
    finally:
        return printed_correctly
