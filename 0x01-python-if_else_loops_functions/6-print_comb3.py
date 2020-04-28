#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if (i != j and i < j):
            if (i != 8 and i != 9):
                print("{:d}".format(i), end="")
                print("{:d}".format(j), end=", ")
            else:
                print("{:d}{:d}".format(i, j))
