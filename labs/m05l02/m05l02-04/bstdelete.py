# Algorithms & Data Structures for Working Engineers — lesson m05l02 — Binary Search Trees: Search, Insert And Delete
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l02
# © LearnSome.tech
class N:
    def __init__(self,v): self.v=v; self.l=self.r=None
def ins(n,v):
    if not n: return N(v)
    if v<n.v: n.l=ins(n.l,v)
    elif v>n.v: n.r=ins(n.r,v)
    return n
def delete(n,v):
    if not n: return None
    if v<n.v: n.l=delete(n.l,v); return n
    if v>n.v: n.r=delete(n.r,v); return n
    if not n.l: return n.r
    if not n.r: return n.l
    s=n.r
    while s.l: s=s.l
    n.v=s.v; n.r=delete(n.r,s.v); return n
def io(n): return []if not n else io(n.l)+[n.v]+io(n.r)
bst=None
for v in [5,3,7,1,4,6,8]: bst=ins(bst,v)
print('initial:', io(bst))
bst=delete(bst,3); print('deleted three:', io(bst))
bst=delete(bst,5); print('deleted five:', io(bst))
