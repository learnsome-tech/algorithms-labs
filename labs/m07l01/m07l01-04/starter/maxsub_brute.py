def max_sub_brute(arr):
    best = arr[0]
    ops = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            ops += 1
            if total > best:
                best = total
    return best, ops

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best, ops = max_sub_brute(arr)
print('best sum:', best)
print('operations:', ops)
print('brute force is quadratic in n')
