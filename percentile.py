def get_percentile(arr, x):
    arr.sort()
    return arr[int(x/100*len(arr))]