# Algorithms & Data Structures for Working Engineers — lesson m05l05 — Heaps And Priority Queues
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l05
# © LearnSome.tech
import heapq

def heap_sort(lst):
    h = list(lst)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

data = [64, 25, 12, 22, 11]
print('original:', data)
print('sorted:', heap_sort(data))
