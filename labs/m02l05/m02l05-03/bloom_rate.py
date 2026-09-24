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

bf = Bloom(128, 3)
inserted = [f'word{i}' for i in range(20)]
for w in inserted: bf.add(w)
probes = [f'test{i}' for i in range(100)]
fp = sum(1 for t in probes if t in bf)
print('false positives:', fp, 'out of', len(probes))
print('false positive rate:', round(fp / len(probes), 2))
