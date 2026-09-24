# Algorithms & Data Structures for Working Engineers — lesson m05l01 — Binary Trees And Their Traversals
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l01
# © LearnSome.tech
class Node:
    def __init__(self, v): self.val=v; self.left=None; self.right=None

def inorder(n, acc):
    if n: inorder(n.left, acc); acc.append(n.val); inorder(n.right, acc)

def preorder(n, acc):
    if n: acc.append(n.val); preorder(n.left, acc); preorder(n.right, acc)

def postorder(n, acc):
    if n: postorder(n.left, acc); postorder(n.right, acc); acc.append(n.val)

r = Node(10); r.left=Node(5); r.right=Node(15)
r.left.left=Node(2); r.left.right=Node(7)
r.right.left=Node(12); r.right.right=Node(20)

io=[]; inorder(r, io); print('inorder:', io)
pre=[]; preorder(r, pre); print('preorder:', pre)
post=[]; postorder(r, post); print('postorder:', post)
