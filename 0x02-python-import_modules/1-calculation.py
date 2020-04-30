#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    summ = add(a, b)
    # adds a and b
    print("{:d} + {:d} = {:d}".format(a, b, summ))
    diff = sub(a, b)
    # subtracts a and b
    print("{:d} - {:d} = {:d}".format(a, b, diff))
    prod = mul(a, b)
    # multiplies a and b
    print("{:d} * {:d} = {:d}".format(a, b, prod))
    quot = div(a, b)
    # divides a and b
    print("{:d} / {:d} = {:d}".format(a, b, quot))
