# Algorithms & Data Structures for Working Engineers — lesson m05l01 — Binary Trees And Their Traversals
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l01
# © LearnSome.tech
class Node:
    def __init__(self, v): self.val=v; self.left=None; self.right=None

def height(n):
    if n is None: return 0
    return 1 + max(height(n.left), height(n.right))

def count(n):
    if n is None: return 0
    return 1 + count(n.left) + count(n.right)

r = Node(10); r.left=Node(5); r.right=Node(15)
r.left.left=Node(2); r.left.right=Node(7)
r.right.left=Node(12); r.right.right=Node(20)

print('height:', height(r))
print('node count:', count(r))
