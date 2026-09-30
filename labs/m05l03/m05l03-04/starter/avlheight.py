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
for n in [15, 127, 1023]:
    avl=None
    for v in range(1, n+1): avl=ins(avl,v)
    print(f'n={n}: avl height {ht(avl)}, sorted bst height {n}')
