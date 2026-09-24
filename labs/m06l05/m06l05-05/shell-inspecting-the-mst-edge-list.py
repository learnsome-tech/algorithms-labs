# Algorithms & Data Structures for Working Engineers — lesson m06l05 — Minimum Spanning Trees: Kruskal And Prim
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

edges = [(1,'A','B'), (2,'B','C'), (4,'B','D')]
sorted(edges)
#   [(1, 'A', 'B'), (2, 'B', 'C'), (4, 'B', 'D')]
sum(w for w,_,_ in edges)
#   7
len(edges)
#   3
