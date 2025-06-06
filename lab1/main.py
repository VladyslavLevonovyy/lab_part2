def is_monotonic(arr):
    if len(arr) <= 1:
        return True

    is_increasing = True
    is_decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            is_decreasing = False
        elif arr[i] < arr[i - 1]:
            is_increasing = False

    return is_increasing or is_decreasing
