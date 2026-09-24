# Algorithms & Data Structures for Working Engineers — lesson m01l02 — Recognising The Common Growth Rates
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l02
# © LearnSome.tech
def nested_ops(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def halving_ops(n):
    count = 0
    size = n
    while size > 1:
        size = size // 2
        count += 1
    return count

for n in [8, 64, 512]:
    print(n, halving_ops(n), nested_ops(n))
