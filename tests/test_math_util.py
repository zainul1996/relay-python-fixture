import unittest

from src.math_util import add, gcd


class MathUtilTest(unittest.TestCase):
    def test_add_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_gcd_of_positive_numbers(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)

    def test_gcd_with_negative_input(self):
        self.assertEqual(gcd(-48, 18), 6)


if __name__ == "__main__":
    unittest.main()
