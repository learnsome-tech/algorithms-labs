# Algorithms & Data Structures for Working Engineers — lesson m02l05 — Bloom Filters: Membership Without The Data
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l05
# © LearnSome.tech
import hashlib

class Bloom:
    def __init__(self, m, k):
        self.bits, self.m, self.k = [False]*m, m, k
    def _idx(self, x):
        return [int(hashlib.sha256(f'{i}:{x}'.encode()).hexdigest(),16)%self.m
                for i in range(self.k)]
    def add(self, x):
        for p in self._idx(x): self.bits[p] = True
    def __contains__(self, x):
        return all(self.bits[p] for p in self._idx(x))

bf = Bloom(64, 3)
words = ['apple', 'banana', 'cherry', 'date']
for w in words: bf.add(w)
for w in words: print(w, 'in filter:', w in bf)
print('elderberry in filter:', 'elderberry' in bf)
print('fig in filter:', 'fig' in bf)
