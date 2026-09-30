import heapq

def heap_sort(lst):
    h = list(lst)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

data = [64, 25, 12, 22, 11]
print('original:', data)
print('sorted:', heap_sort(data))
