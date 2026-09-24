# Algorithms & Data Structures for Working Engineers — lesson m06l01 — Representing A Graph: Matrix Or Adjacency List
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l01
# © LearnSome.tech
nodes = ['A', 'B', 'C', 'D', 'E']
idx = {n: i for i, n in enumerate(nodes)}

matrix = [[0] * 5 for _ in range(5)]
for u, v in [('A','B'),('A','C'),('B','D'),('B','E'),('C','D')]:
    matrix[idx[u]][idx[v]] = 1
    matrix[idx[v]][idx[u]] = 1

print('A neighbours:', [nodes[j] for j, x in enumerate(matrix[0]) if x])
print('B neighbours:', [nodes[j] for j, x in enumerate(matrix[1]) if x])
print('matrix cells:', len(nodes) ** 2)
