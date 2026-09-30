import bisect
T = 2
class N:
    def __init__(self,lf=True): self.k=[];self.c=[];self.lf=lf
    def full(self): return len(self.k)==2*T-1
def sp(p,i):
    y=p.c[i]; m=y.k[T-1]; z=N(y.lf)
    z.k=y.k[T:];y.k=y.k[:T-1]
    if not y.lf: z.c=y.c[T:];y.c=y.c[:T]
    p.k.insert(i,m);p.c.insert(i+1,z)
def nf(n,k):
    i=bisect.bisect_left(n.k,k)
    if n.lf: n.k.insert(i,k);return
    if n.c[i].full(): sp(n,i);i+=(k>n.k[i])
    nf(n.c[i],k)
def ins(rt,k):
    if rt.full():
        s=N(False);s.c=[rt];sp(s,0);nf(s,k);return s
    nf(rt,k);return rt
r=N()
for v in [5,3,7,1,4,6,8,2]: r=ins(r,v)
print('root keys:',r.k,'children:',[c.k for c in r.c])
