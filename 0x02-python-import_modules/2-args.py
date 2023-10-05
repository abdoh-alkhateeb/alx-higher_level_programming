#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    print("{:d} arguments".format(argc - 1), end="")
    if argc - 1:
        print(":")
        for i in range(1, argc):
            print("{:d}: {:s}".format(i, argv[i]))
    else:
        print(".")
