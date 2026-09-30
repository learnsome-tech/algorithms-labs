import random
def merge_sort(arr):
    count = [0]
    def merge(L, R):
        out = []; i = j = 0
        while i < len(L) and j < len(R):
            count[0] += 1
            if L[i] <= R[j]: out.append(L[i]); i += 1
            else: out.append(R[j]); j += 1
        return out + L[i:] + R[j:]
    def sort(a):
        if len(a) <= 1: return a[:]
        m = len(a) // 2
        return merge(sort(a[:m]), sort(a[m:]))
    return sort(arr), count[0]
random.seed(1)
data = [random.randint(0, 99) for _ in range(10)]
result, c = merge_sort(data)
print('before:', data)
print('sorted:', result)
print('comparisons:', c)
print('verified:', result == sorted(data))
