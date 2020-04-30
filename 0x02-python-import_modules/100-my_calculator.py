#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if (len(argv) == 4):
        a = int(argv[1])
        b = int(argv[3])
        summ = add(a, b)
        diff = sub(a, b)
        prod = mul(a, b)
        quot = div(a, b)
        if (argv[2] == "+"):
            print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, summ))
        elif (argv[2] == "-"):
            print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, diff))
        elif (argv[2] == "*"):
            print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, prod))
        elif (argv[2] == "/"):
            print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, quot))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
