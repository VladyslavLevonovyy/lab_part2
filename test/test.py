import unittest
from src.career import max_experience


class TestCareer(unittest.TestCase):
    def test_small_pyramid(self):
        pyramid = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(max_experience(pyramid), 12)

    def test_single_level(self):
        pyramid = [[7]]
        self.assertEqual(max_experience(pyramid), 7)

    def test_all_zeros(self):
        pyramid = [
            [0],
            [0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(max_experience(pyramid), 0)


if __name__ == "__main__":
    unittest.main()
