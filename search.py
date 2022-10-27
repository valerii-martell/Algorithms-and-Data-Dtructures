def binary_search(arr, elem, start, end):

    middle = (start + end) // 2

    # print("------")
    # print(start)
    # print(end)
    # print(middle)

    if arr[middle] == elem:
        return middle
    elif arr[middle] < elem:
        return binary_search(arr, elem, middle + 1, end)
    elif arr[middle] > elem:
        return binary_search(arr, elem, start, middle - 1)
    else:
        return -1
