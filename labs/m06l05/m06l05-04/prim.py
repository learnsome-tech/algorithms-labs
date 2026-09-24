# Algorithms & Data Structures for Working Engineers — lesson m06l05 — Minimum Spanning Trees: Kruskal And Prim
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l05
# © LearnSome.tech
import heapq
G = {
    'A': [('B',1),('C',3)],
    'B': [('A',1),('C',2),('D',4)],
    'C': [('A',3),('B',2),('D',5)],
    'D': [('B',4),('C',5)],
}
visited, total = {'A'}, 0
heap = [(w,v) for v,w in G['A']]
heapq.heapify(heap)
while heap:
    w, v = heapq.heappop(heap)
    if v in visited:
        continue
    visited.add(v)
    print('add edge to', v, 'weight', w)
    total += w
    for nb, nb_w in G[v]:
        if nb not in visited:
            heapq.heappush(heap, (nb_w, nb))
print('total:', total)
