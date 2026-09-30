from collections import deque

class Node:
    def __init__(self, v): self.val=v; self.left=None; self.right=None

def levelorder(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        n = q.popleft()
        result.append(n.val)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return result

r = Node(10); r.left=Node(5); r.right=Node(15)
r.left.left=Node(2); r.left.right=Node(7)
r.right.left=Node(12); r.right.right=Node(20)

print('level-order:', levelorder(r))
