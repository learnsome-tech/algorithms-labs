# Algorithms & Data Structures for Working Engineers — lesson m05l02 — Binary Search Trees: Search, Insert And Delete
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l02
# © LearnSome.tech
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, v):
    if root is None: return Node(v)
    if v < root.val: root.left = insert(root.left, v)
    elif v > root.val: root.right = insert(root.right, v)
    return root

def inorder(n, out):
    if n: inorder(n.left, out); out.append(n.val); inorder(n.right, out)

bst = None
for v in [5, 3, 7, 1, 4, 6, 8]: bst = insert(bst, v)
result = []; inorder(bst, result)
print('in-order:', result)
print('root:', bst.val)
print('root left:', bst.left.val, 'right:', bst.right.val)
