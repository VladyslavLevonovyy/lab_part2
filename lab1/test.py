import unittest
from monotonic import is_monotonic

class TestMonotonic(unittest.TestCase):
    def test_strictly_increasing(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5]))

    def test_strictly_decreasing(self):
        self.assertTrue(is_monotonic([10, 8, 6, 4, 2]))

    def test_equal_values(self):
        self.assertTrue(is_monotonic([7, 7, 7, 7]))

    def test_mixed_direction(self):
        self.assertFalse(is_monotonic([1, 3, 2, 4]))

    def test_single_element(self):
        self.assertTrue(is_monotonic([100]))

    def test_empty_array(self):
        self.assertTrue(is_monotonic([]))

if __name__ == "__main__":
    unittest.main()
