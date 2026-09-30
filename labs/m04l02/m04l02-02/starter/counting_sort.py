def counting_sort(arr, k):
    counts = [0] * k
    for v in arr:
        counts[v] += 1
    result = []
    for v, c in enumerate(counts):
        result.extend([v] * c)
    return result

import random
random.seed(1)
data = [random.randint(0, 9) for _ in range(12)]
print('input: ', data)
result = counting_sort(data, 10)
print('sorted:', result)
print('verified:', result == sorted(data))
