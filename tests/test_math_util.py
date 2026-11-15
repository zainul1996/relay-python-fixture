import unittest

from src.math_util import add


class MathUtilTest(unittest.TestCase):
    def test_add_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
