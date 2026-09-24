# Algorithms & Data Structures for Working Engineers — lesson m04l02 — Counting And Radix Sort: Beating N Log N
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

data = [4, 2, 1, 4, 2, 3]
counts = [0] * 5
for v in data: counts[v] += 1
counts
#   [0, 1, 2, 1, 2]
[v for v in range(5) for _ in range(counts[v])]
#   [1, 2, 2, 3, 4, 4]
sorted(data)
#   [1, 2, 2, 3, 4, 4]
