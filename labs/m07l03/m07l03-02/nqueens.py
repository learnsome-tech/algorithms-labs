# Algorithms & Data Structures for Working Engineers — lesson m07l03 — Backtracking: Search With Pruning
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l03
# © LearnSome.tech
def queens(n, row=0, used=(), d1=(), d2=()):
    if row == n:
        return 1, used
    count = 0
    first = None
    for col in range(n):
        if col not in used and row-col not in d1 and row+col not in d2:
            c, f = queens(n, row+1,
                used+(col,), d1+(row-col,), d2+(row+col,))
            count += c
            if first is None:
                first = f
    return count, first

for n in [4, 5, 6, 7, 8]:
    count, first = queens(n)
    print(f'n={n}: {count} solutions, e.g. {list(first)}')
