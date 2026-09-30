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

for m in [64, 128, 512]:
    bf = Bloom(m, 3)
    for i in range(20): bf.add(f'word{i}')
    fp = sum(1 for i in range(100) if f'test{i}' in bf)
    print(f'm={m}: {fp} false positives per hundred')
