# Algorithms & Data Structures for Working Engineers — lesson m06l01 — Representing A Graph: Matrix Or Adjacency List
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l01
# © LearnSome.tech
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['B'],
}

for node, neighbours in graph.items():
    print(node, '->', neighbours)

edges = sum(len(v) for v in graph.values()) // 2
print('edges:', edges)
