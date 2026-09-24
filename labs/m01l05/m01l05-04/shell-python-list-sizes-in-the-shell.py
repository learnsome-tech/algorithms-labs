# Algorithms & Data Structures for Working Engineers — lesson m01l05 — Amortised Analysis: Why Append Is Cheap
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import sys
lst = []
sys.getsizeof(lst)
#   56
for i in range(9): lst.append(i)
len(lst), sys.getsizeof(lst)
#   (9, 184)
for i in range(9): lst.append(i)
len(lst), sys.getsizeof(lst)
#   (18, 248)
