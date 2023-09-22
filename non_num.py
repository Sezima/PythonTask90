'find the first non-consecutive number'
def first_non_consecutive(arr):
    c = 1
    for i in arr:
        if c < len(arr) and arr[c] - arr[c-1] != 1:
            return arr[c]
        c += 1
    return None