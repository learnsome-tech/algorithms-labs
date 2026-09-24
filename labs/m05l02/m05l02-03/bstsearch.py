# Algorithms & Data Structures for Working Engineers — lesson m05l02 — Binary Search Trees: Search, Insert And Delete
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l02
# © LearnSome.tech
class N:
    def __init__(self, v): self.v=v; self.l=None; self.r=None

def ins(n,v):
    if n is None: return N(v)
    if v < n.v: n.l = ins(n.l, v)
    elif v > n.v: n.r = ins(n.r, v)
    return n

def find(n, v):
    if n is None: return False
    if v == n.v: return True
    return find(n.l if v < n.v else n.r, v)

def mini(n):
    while n.l: n = n.l
    return n.v
bst = None
for v in [5, 3, 7, 1, 4]: bst = ins(bst, v)
print('find five:', find(bst, 5))
print('find nine:', find(bst, 9))
print('minimum:', mini(bst))
