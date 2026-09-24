# Algorithms & Data Structures for Working Engineers — lesson m06l05 — Minimum Spanning Trees: Kruskal And Prim
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l05
# © LearnSome.tech
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True
uf = UF(4)
for x, y in [(0,1),(2,3),(1,2)]:
    uf.union(x, y)
print([uf.find(i) for i in range(4)])
