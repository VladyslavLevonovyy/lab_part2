import math


def calculate_max_wire_length(w, heights):
    n = len(heights)
    min_len = [0] * n
    max_len = [0] * n

    for i in range(1, n):
        dx = w
        from_min = min_len[i - 1] + math.hypot(dx, 0)
        from_max = max_len[i - 1] + math.hypot(dx, heights[i - 1] - 1)
        min_len[i] = max(from_min, from_max)

        from_min = min_len[i - 1] + math.hypot(dx, heights[i] - 1)
        from_max = max_len[i - 1] + \
            math.hypot(dx, abs(heights[i] - heights[i - 1]))
        max_len[i] = max(from_min, from_max)

    result = max(min_len[-1], max_len[-1])
    return round(result, 2)


if __name__ == "__main__":
    w = 2
    heights = [3, 3, 3]
    result = calculate_max_wire_length(w, heights)
    print(result)
