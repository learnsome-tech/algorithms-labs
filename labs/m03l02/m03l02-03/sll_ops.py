# Algorithms & Data Structures for Working Engineers — lesson m03l02 — Linked Lists: Nodes, Pointers And Sentinels
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l02
# © LearnSome.tech
class Node:
    def __init__(self, v): self.val=v; self.next=None
def push(head, v):
    n=Node(v); n.next=head; return n
def delete(head, v):
    if head and head.val==v: return head.next
    c=head
    while c and c.next:
        if c.next.val==v: c.next=c.next.next; break
        c=c.next
    return head
def find(head, v):
    c=head
    while c and c.val!=v: c=c.next
    return c is not None
def show(head):
    c,r=head,[]
    while c: r.append(str(c.val)); c=c.next
    print(' -> '.join(r))
head=None
for v in [30,20,10]: head=push(head,v)
show(head);head=delete(head,20);show(head);print(find(head,10),find(head,20))
