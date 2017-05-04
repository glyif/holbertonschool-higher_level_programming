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

    argc = len(sys.argv)

    if argc < 3:
        print_error(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        result = calculator_1.add(a, b)
        print_result(a, op, b, result)
    elif op == '-':
        result = calculator_1.sub(a, b)
        print_result(a, op, b, result)
    elif op == '*':
        result = calculator_1.mul(a, b)
        print_result(a, op, b, result)
    elif op == '/':
        result = calculator_1.div(a, b)
        print_result(a, op, b, result)
    else:
        print_error(2)
