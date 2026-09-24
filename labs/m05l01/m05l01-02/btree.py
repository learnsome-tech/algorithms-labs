# Algorithms & Data Structures for Working Engineers — lesson m05l01 — Binary Trees And Their Traversals
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l01
# © LearnSome.tech
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print('root:', root.val)
print('left subtree root:', root.left.val)
print('right subtree root:', root.right.val)
print('deepest left leaf:', root.left.left.val)
