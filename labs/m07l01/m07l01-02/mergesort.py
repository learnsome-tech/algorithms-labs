# Algorithms & Data Structures for Working Engineers — lesson m07l01 — Divide And Conquer And The Recurrence
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l01
# © LearnSome.tech
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

data = [5, 2, 8, 1, 9, 3]
print(merge_sort(data))
