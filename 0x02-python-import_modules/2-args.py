#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    print("{} argument{}".format(argc - 1, "s" if argc != 2 else ""), end="")
    if argc - 1:
        print(":")
        for i in range(1, argc):
            print("{:d}: {:s}".format(i, argv[i]))
    else:
        print(".")
