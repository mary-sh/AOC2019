import unittest

import day_1


class Day1TestCase(unittest.TestCase):
    def test_1(self):
        assert day_1.calculate_required_fuel(12) == 2

    def test_2(self):
        assert day_1.calculate_required_fuel(14) == 2

    def test_3(self):
        assert day_1.calculate_required_fuel(1969) == 654

    def test_4(self):
        assert day_1.calculate_required_fuel(100756) == 33583


unittest.main()
