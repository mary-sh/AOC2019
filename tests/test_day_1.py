import unittest

import day_1


class Day1TestCase(unittest.TestCase):
    def test_1(self):
        assert day_1.calculate_required_fuel(12) == 2

    def test_2(self):
        assert day_1.calculate_required_fuel(14) == 2
        assert day_1.calculate_fuel_for_fuel(2) == 0

    def test_3(self):
        assert day_1.calculate_required_fuel(1969) == 654
        assert day_1.calculate_fuel_for_fuel(654) == 966 - 654

    def test_4(self):
        assert day_1.calculate_required_fuel(100756) == 33583
        assert day_1.calculate_fuel_for_fuel(33583) == 50346 - 33583


if __name__ == '__main__':
    unittest.main()
