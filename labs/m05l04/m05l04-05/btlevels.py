# Algorithms & Data Structures for Working Engineers — lesson m05l04 — B-Trees: The Structure Behind Every Database Index
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l04
# © LearnSome.tech
from collections import deque

class Node:
    def __init__(self, k, c=None, lf=True): self.k=k; self.c=c or []; self.lf=lf

def by_level(root):
    q=deque([(root,0)]); rows={}
    while q:
        n,d=q.popleft(); rows.setdefault(d,[]).extend(n.k)
        if not n.lf: [q.append((c,d+1)) for c in n.c]
    return rows

a,b,c,d_ = Node([1]),Node([3]),Node([5]),Node([7])
p=Node([2],[a,b],False); q_=Node([6],[c,d_],False)
root=Node([4],[p,q_],False)

for depth,keys in sorted(by_level(root).items()):
    print('level', depth, ':', keys)
