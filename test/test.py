import unittest
from src.main import minimum_cable_length


class TestMinimumCableLength(unittest.TestCase):
    def test_connected_graph(self):
        test_file = "test/test_data_connected.csv"
        with open(test_file, "w") as f:
            f.write("A,B,1\nB,C,2\nC,D,3\nD,A,4\n")

        result = minimum_cable_length(test_file)
        self.assertEqual(result, 6)

    def test_disconnected_graph(self):
        test_file = "test/test_data_disconnected.csv"
        with open(test_file, "w") as f:
            f.write("A,B,1\nC,D,2\n")

        result = minimum_cable_length(test_file)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
