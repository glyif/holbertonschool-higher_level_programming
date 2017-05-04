#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import calculator_1

    def print_error(n):
        if n is 1:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)
        elif n is 2:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

    def print_result(a, op, b, result):
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))

    router = {
            '+': calculator_1.add,
            '-': calculator_1.sub,
            '*': calculator_1.mul,
            '/': calculator_1.div
            }


    argc = len(sys.argv)

    if argc <= 3:
        print_error(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    for key in router:
        if op == key:
            result = router[op](a, b)
            print_result(a, op, b, result)
            sys.exit(0)

    print_error(2)
