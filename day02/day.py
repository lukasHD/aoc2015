# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os

import helper.helper as helper


def alg1(data, print_debug):
    """Runs algo for first part of the day"""
    result = 0
    for line in data:
        sides = []
        values = list(map(int, line.split("x")))
        sides.append(values[0] * values[1])
        sides.append(values[0] * values[2])
        sides.append(values[1] * values[2])
        print(sides)
        result += 2*sum(sides) + min(sides)

    return result


def alg2(data, print_debug):
    """Runs algo for second part of the day"""
    result = 0
    for line in data:
        sides = []
        values = list(map(int, line.split("x")))
        sides.append(values[0])
        sides.append(values[1])
        sides.append(values[2])
        sides.sort()

        thisone = 2*sides[0] + 2*sides[1] + sides[0]*sides[1]*sides[2]
        print(f"{sides} --> {thisone}")
        result += thisone
    return result


def part1(fname: str, print_debug = False):
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

def part2(fname: str, print_debug = False):
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


if __name__ == '__main__':
    print(os.path.normpath(__file__))
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')

    print("--- Day 2: I Was Told There Would Be No Math ---\n")
    # part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
