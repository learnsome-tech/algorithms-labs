# Algorithms & Data Structures for Working Engineers — lesson m06l02 — Breadth-First Search And Shortest Paths By Hops
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l02
# © LearnSome.tech
from collections import deque
G = {'Alice': ['Bob','Carol'], 'Bob': ['Alice','Dave'],
     'Carol': ['Alice','Dave'], 'Dave': ['Bob','Carol']}
def bfs_layers(G, src):
    dist = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in G[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    layers = {}
    for node, d in dist.items():
        layers.setdefault(d, []).append(node)
    for d in sorted(layers):
        print('layer', d, ':', layers[d])
bfs_layers(G, 'Alice')
