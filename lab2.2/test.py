import unittest
from main import minimum_time


class TestMinimumTime(unittest.TestCase):
    def test_1(self):
        K = 10
        T = 5
        lengths = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        self.assertEqual(minimum_time(K, T, lengths), 100)


if __name__ == "__main__":
    unittest.main()
