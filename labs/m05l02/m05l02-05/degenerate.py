# Algorithms & Data Structures for Working Engineers — lesson m05l02 — Binary Search Trees: Search, Insert And Delete
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l02
# © LearnSome.tech
class Node:
    def __init__(self, v): self.val=v; self.left=None; self.right=None

def insert(root, v):
    if root is None: return Node(v)
    if v < root.val: root.left = insert(root.left, v)
    elif v > root.val: root.right = insert(root.right, v)
    return root

def height(n):
    if n is None: return 0
    return 1 + max(height(n.left), height(n.right))

bst1 = None
for v in [4, 2, 6, 1, 3, 5, 7]: bst1 = insert(bst1, v)

bst2 = None
for v in range(1, 8): bst2 = insert(bst2, v)

print('balanced insert height:', height(bst1))
print('sorted insert height:', height(bst2))
print('sorted is linear in n:', height(bst2) == 7)
