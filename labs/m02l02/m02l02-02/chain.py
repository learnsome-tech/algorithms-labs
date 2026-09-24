# Algorithms & Data Structures for Working Engineers — lesson m02l02 — Hash Tables: Chaining, Open Addressing And Load Factor
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l02
# © LearnSome.tech
import hashlib

def slot(k, n):
    return int(hashlib.sha256(str(k).encode()).hexdigest(), 16) % n

class ChainMap:
    def __init__(self, n=8):
        self.n, self.b = n, [[] for _ in range(n)]
    def put(self, k, v):
        s = slot(k, self.n)
        for p in self.b[s]:
            if p[0] == k: p[1] = v; return
        self.b[s].append([k, v])
    def get(self, k):
        for p in self.b[slot(k, self.n)]:
            if p[0] == k: return p[1]

m = ChainMap()
for w in ['ant', 'bee', 'cat', 'dog', 'elk', 'fox']:
    m.put(w, len(w))
print([len(b) for b in m.b])
print(m.get('cat'))
