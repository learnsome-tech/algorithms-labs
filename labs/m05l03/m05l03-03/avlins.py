# Algorithms & Data Structures for Working Engineers — lesson m05l03 — AVL Trees: Rotations That Keep The Guarantee
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l03
# © LearnSome.tech
class AVL:
    def __init__(self,v): self.v=v; self.l=self.r=None; self.h=1
def ht(n): return n.h if n else 0
def fix(n): n.h=1+max(ht(n.l),ht(n.r))
def bf(n): return ht(n.l)-ht(n.r)
def rr(y): x=y.l; y.l=x.r; x.r=y; fix(y); fix(x); return x
def rl(x): y=x.r; x.r=y.l; y.l=x; fix(x); fix(y); return y
def ins(n,v):
    if not n: return AVL(v)
    if v<n.v: n.l=ins(n.l,v)
    else: n.r=ins(n.r,v)
    fix(n); b=bf(n)
    if b>1 and v<n.l.v: return rr(n)
    if b<-1 and v>n.r.v: return rl(n)
    if b>1: n.l=rl(n.l); return rr(n)
    if b<-1: n.r=rr(n.r); return rl(n)
    return n
t=None
for v in [1,3,2]: t=ins(t,v)
print('after rl rotation, root:', t.v, 'height:', ht(t))
print('root bf:', bf(t), 'left:', t.l.v, 'right:', t.r.v)
