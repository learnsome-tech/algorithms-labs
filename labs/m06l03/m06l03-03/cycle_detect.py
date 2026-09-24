# Algorithms & Data Structures for Working Engineers — lesson m06l03 — Depth-First Search, Cycles And Topological Order
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l03
# © LearnSome.tech
def has_cycle(G):
    color = {n: 'white' for n in G}
    def dfs(u):
        color[u] = 'gray'
        for v in G[u]:
            if color[v] == 'gray':
                return True
            if color[v] == 'white' and dfs(v):
                return True
        color[u] = 'black'
        return False
    return any(dfs(n) for n in G if color[n] == 'white')

dag = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
cyclic = {'A': ['B'], 'B': ['C'], 'C': ['A']}
print('dag has cycle:', has_cycle(dag))
print('cyclic has cycle:', has_cycle(cyclic))
