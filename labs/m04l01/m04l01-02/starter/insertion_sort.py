import random
def insertion_sort(arr):
    ct = [0]
    def sort(a):
        for i in range(1, len(a)):
            key = a[i]; j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]; j -= 1; ct[0] += 1
            a[j + 1] = key
    work = arr[:]
    sort(work)
    return work, ct[0]
random.seed(1)
data = [random.randint(0, 99) for _ in range(10)]
result, c = insertion_sort(data)
print('before:', data)
print('sorted:', result)
print('comparisons:', c)
print('verified:', result == sorted(data))
