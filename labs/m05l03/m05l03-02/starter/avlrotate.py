class AVL:
    def __init__(self, v): self.v=v; self.l=self.r=None; self.h=1
def ht(n): return n.h if n else 0
def fix(n): n.h=1+max(ht(n.l),ht(n.r))
def bf(n): return ht(n.l)-ht(n.r)
def rl(x):
    y=x.r; x.r=y.l; y.l=x; fix(x); fix(y); return y

root = AVL(1)
root.r = AVL(2)
root.r.r = AVL(3)
fix(root.r); fix(root)

print('before rotation, bf at root:', bf(root))
new_root = rl(root)
print('after left rotation, root value:', new_root.v)
print('left child:', new_root.l.v, 'right child:', new_root.r.v)
print('new root height:', ht(new_root))
