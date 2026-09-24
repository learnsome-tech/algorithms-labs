# Algorithms & Data Structures for Working Engineers — lesson m02l01 — What A Hash Function Promises
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l01
# © LearnSome.tech
def poly_hash(key, n, base=31):
    h = 0
    for ch in key:
        h = (h * base + ord(ch)) % n
    return h

words = ['ant', 'bee', 'cat', 'dog', 'elk',
         'fox', 'gnu', 'hen']
counts = [0] * 8
for w in words:
    counts[poly_hash(w, 8)] += 1
for i, c in enumerate(counts):
    print(f'bucket {i}: {c}')
