def sort_decorator(func):
    def wrapper(arg):
        result = arg
        func(result)
        return result
    return wrapper


def bubble_sort(arr):
    result = list.copy(arr)
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def insertion_sort(arr):
    result = list.copy(arr)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and key < result[j]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def selection_sort(arr):
    result = list.copy(arr)
    for i in range(len(result) - 1):
        index_min = i
        for j in range(i + 1, len(result)):
            if result[j] < result[index_min]:
                index_min = j
        result[i], result[index_min] = result[index_min], result[i]
    return result


def counting_sort(arr):
    result = [0 for _ in range(len(arr))]
    count = [0 for _ in range(100)]

    for i in range(len(arr)):
        count[arr[i]] += 1

    startings = count
    for i in range(1, len(count)):
        startings[i] += startings[i-1]
    for i in range(len(startings)-1, 0, -1):
        startings[i] = startings[i-1]
    startings[0] = 0

    for i in range(len(arr)):
        result[startings[arr[i]]] = arr[i]
        startings[arr[i]] += 1

    return result


def merge_sort(arr):
    result = list.copy(arr)

    def _merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            l = arr[:mid]
            r = arr[mid:]

            _merge_sort(l)
            _merge_sort(r)

            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1
                else:
                    arr[k] = r[j]
                    j += 1
                k += 1

            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1

    _merge_sort(result)

    return result


def quick_sort(arr):
    result = list.copy(arr)

    def _quick_sort(arr, left, right):
        i, j = left, right
        pivot = arr[(i + j) // 2]

        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1

            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        if left < j:
            _quick_sort(arr, left, j)
        if i < right:
            _quick_sort(arr, i, right)

    _quick_sort(result, 0, len(result)-1)

    return result


def heap_sort(arr):
    result = list.copy(arr)

    def _get_parent_index(i):
        return (i - 1) // 2

    def _get_left_child_index(i):
        return 2*i+1

    def _get_right_child_index(i):
        return 2*i+2

    def _max_heapify(arr, heapsize, i):
        l = _get_left_child_index(i)
        r = _get_right_child_index(i)

        largest = i
        if l < heapsize and arr[largest] < arr[l]:
            largest = l
        if r < heapsize and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _max_heapify(arr, heapsize, largest)

    def _build_heap(arr, heapsize):
        for i in range(heapsize//2 - 1, -1, -1):
            _max_heapify(arr, heapsize, i)

    def _heap_sort(arr):
        heapsize = len(arr)
        _build_heap(arr, heapsize)
        for i in range(heapsize - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            _max_heapify(arr, i, 0)

    _heap_sort(result)

    return result


def sort_logs(logs):
    result = []

    dig_logs, let_logs = [], []

    def _is_digit(log):
        entries = log.split(" ")
        del entries[0]
        for entry in entries:
            if not entry.isdigit():
                return False
        return True

    for log in logs:
        if _is_digit(log):
            dig_logs.append(log)
        else:
            let_logs.append(log)

    let_logs.sort(key=lambda s: s.split(" ", 1)[1])

    for let_log in let_logs:
        result.append(let_log)

    for dig_log in dig_logs:
        result.append(dig_log)

    return result