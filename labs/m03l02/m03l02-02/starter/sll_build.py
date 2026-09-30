class Node:
    def __init__(self, v): self.val=v; self.next=None
class SLL:
    def __init__(self): self.head=None
    def push_front(self, v):
        n=Node(v); n.next=self.head; self.head=n
    def append(self, v):
        n=Node(v)
        if not self.head: self.head=n; return
        c=self.head
        while c.next: c=c.next
        c.next=n
    def show(self):
        c,r=self.head,[]
        while c: r.append(str(c.val)); c=c.next
        print(' -> '.join(r))
ll=SLL()
ll.append(10)
ll.append(20)
ll.append(30)
ll.push_front(5)
ll.show()
