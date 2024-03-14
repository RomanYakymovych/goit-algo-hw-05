def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    counter = 0
    upper_bound = None

    if x > arr[-1]:
        raise ValueError("Target value is greater than all elements in the array")
    elif x < arr[0]:
        raise ValueError("Target value is smaller than all elements in the array")

    while low <= high:
        counter += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return counter, arr[mid]

    return counter, upper_bound


if __name__ == "__main__":
    arr = [3.5, 4.1, 10.3, 40.5, 50.2, 60.5, 70.1, 80.4, 90.9, 100.0]
    x = 55.0

    try:
        iterations, upper_bound = binary_search(arr, x)
        print(
            f"Було проведено {iterations} ітерацій. Верхня межа становить {upper_bound}"
        )
    except ValueError as e:
        print(e)
