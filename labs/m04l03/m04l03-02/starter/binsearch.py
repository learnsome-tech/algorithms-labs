def binary_search(arr, target):
    # Invariant: target is in arr[lo..hi] if present
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print('find 7:', binary_search(data, 7))
print('find 12:', binary_search(data, 12))
print('find 1:', binary_search(data, 1))
print('find 19:', binary_search(data, 19))
