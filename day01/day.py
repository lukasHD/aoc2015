# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os

import helper.helper as helper


def alg1(data, print_debug):
    """Runs algo for first part of the day"""
    result = 0
    for el in data[0]:
        if el == "(":
            result += 1
        elif el == ")":
            result -= 1
        else:
            raise ValueError
    return result


def alg2(data, print_debug):
    """Runs algo for second part of the day"""
    result = 0
    for i, el in enumerate(data[0]):
        if el == "(":
            result += 1
        elif el == ")":
            result -= 1
        else:
            raise ValueError
        if result == -1:
            return i + 1
    return None


def part1(fname: str, print_debug=False):
    """Wrapper for the first Part. Loads data and sets debug output

    Args:
        fname (str): filename of inputfile
        print_debug (bool, optional): print debug output. Defaults to False.
    """
    print("=== PART 1 ===")
    print(f"-- {fname} --")
    result = 0
    result = alg1(helper.input_as_lines(fname), print_debug)
    print(f"Result = {result}")
    print()


def part2(fname: str, print_debug=False):
    """Wrapper for the second Part. Loads data and sets debug output

    Args:
        fname (str): filename of inputfile
        print_debug (bool, optional): print debug output. Defaults to False.
    """
    print("=== PART 2 ===")
    print(f"-- {fname} --")
    result = 0
    result = alg2(helper.input_as_lines(fname), print_debug)
    print(f"Result = {result}")
    print()


def main():
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')

    print("--- Day 1: Not Quite Lisp ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)


if __name__ == '__main__':
    main()
