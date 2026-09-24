# Algorithms & Data Structures for Working Engineers — lesson m04l05 — Searching With Hashes Versus Trees
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import bisect
a = [10, 20, 30, 40, 50]
bisect.bisect_left(a, 25)
#   2
bisect.bisect_right(a, 30)
#   3
bisect.insort(a, 35)
a
#   [10, 20, 30, 35, 40, 50]
a[bisect.bisect_left(a,25):bisect.bisect_right(a,45)]
#   [30, 35, 40]
