def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    counter = 0
    upper_bound = None

    if x > arr[-1]:
        raise ValueError(
            "Target value is greater than all elements in the array"
        )
    elif x < arr[0]:
        raise ValueError(
            "Target value is smaller than all elements in the array"
        )

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
    arr = [3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    x = 0

    print(
        f"Було проведено {binary_search(arr, x)[0]} ітерацій:ї. Верхня межа становить {binary_search(arr, x)[1]}"
    )
