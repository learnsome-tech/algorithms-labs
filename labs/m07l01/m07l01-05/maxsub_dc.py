# Algorithms & Data Structures for Working Engineers — lesson m07l01 — Divide And Conquer And The Recurrence
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l01
# © LearnSome.tech
def max_cross(arr, lo, mid, hi):
    s, best = 0, float('-inf')
    for i in range(mid, lo-1, -1):
        s += arr[i]; best = max(best, s)
    left = best
    s, best = 0, float('-inf')
    for i in range(mid+1, hi+1):
        s += arr[i]; best = max(best, s)
    return left + best

def max_sub(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo == hi: return arr[lo]
    mid = (lo + hi) // 2
    return max(max_sub(arr, lo, mid),
               max_sub(arr, mid+1, hi),
               max_cross(arr, lo, mid, hi))

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print('best sum:', max_sub(arr))
print('divide and conquer is order n log n')
