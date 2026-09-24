# Algorithms & Data Structures for Working Engineers — lesson m06l04 — Dijkstra: Shortest Paths With A Priority Queue
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import heapq
h = []
heapq.heappush(h, (3, 'B'))
heapq.heappush(h, (1, 'A'))
heapq.heappush(h, (4, 'C'))
heapq.heappop(h)
#   (1, 'A')
heapq.heappop(h)
#   (3, 'B')
