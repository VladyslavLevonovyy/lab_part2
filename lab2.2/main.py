import unittest


def minimum_time(K, T, lengths):

    max_length = max(lengths)
    total_length = sum(lengths)

    while max_length < total_length:
        mid = (max_length + total_length) // 2
        painters = 1
        current_length = 0

        for length in lengths:
            if current_length + length > mid:
                painters += 1
                current_length = length
            else:
                current_length += length

        if painters > K:
            max_length = mid + 1
        else:
            total_length = mid

    return max_length * T


print(minimum_time(2, 2, [10, 8, 19]))


def test_1(self):
    K = 2
    T = 2
    lengths = [10, 8, 19]
    self.assertEqual(minimum_time(K, T, lengths))

    if __name__ == "__main__":
        unittest.main()
