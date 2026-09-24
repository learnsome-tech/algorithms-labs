# Algorithms & Data Structures for Working Engineers — lesson m05l04 — B-Trees: The Structure Behind Every Database Index
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l04
# © LearnSome.tech
T = 2  # nodes hold 1..3 keys

def search(node, k):
    keys, children, leaf = node
    i = 0
    while i < len(keys) and k > keys[i]: i += 1
    if i < len(keys) and keys[i] == k: return True
    return False if leaf else search(children[i], k)

n1=([1],[],True); n2=([3],[],True)
n3=([5],[],True); n4=([7],[],True)
nl=([2],[n1,n2],False); nr=([6],[n3,n4],False)
root=([4],[nl,nr],False)

for k in [1, 4, 5, 9]:
    print('search', k, ':', search(root, k))
