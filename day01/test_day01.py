from unittest import TestCase

import os
import day01.day
import helper.helper as helper


class Test(TestCase):
    test_filename = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_filename = os.path.join(os.path.dirname(__file__), 'input.txt')

    def test_part1(self):
        self.assertEqual(day01.day.alg1(helper.input_as_lines(self.input_filename), False), 138)

    def test_part2(self):
        self.assertEqual(day01.day.alg2(helper.input_as_lines(self.input_filename), False), 1771)
