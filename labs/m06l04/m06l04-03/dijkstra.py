# Algorithms & Data Structures for Working Engineers — lesson m06l04 — Dijkstra: Shortest Paths With A Priority Queue
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l04
# © LearnSome.tech
import heapq
G = {'A': [('B',4),('C',2)], 'B': [('D',5),('E',1)],
     'C': [('B',1),('D',8)], 'D': [('E',2)], 'E': []}
def dijkstra(G, src):
    dist = {src: 0}
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float('inf')):
            continue
        for v, w in G[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist
for node, d in dijkstra(G, 'A').items():
    print(node, 'distance', d)
