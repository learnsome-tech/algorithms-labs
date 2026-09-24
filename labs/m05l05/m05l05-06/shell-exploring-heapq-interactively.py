# Algorithms & Data Structures for Working Engineers — lesson m05l05 — Heaps And Priority Queues
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import heapq
h = [4, 1, 7, 3]
heapq.heapify(h)
h
#   [1, 3, 7, 4]
heapq.heappush(h, 2)
heapq.heappop(h)
#   1
heapq.nsmallest(2, h)
#   [2, 3]
