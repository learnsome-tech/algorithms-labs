class Node:
    def __init__(self, v): self.val=v; self.next=None
class SentinelList:
    def __init__(self): self.sent=Node(None)
    def push_front(self, v):
        n=Node(v); n.next=self.sent.next; self.sent.next=n
    def append(self, v):
        n=Node(v); c=self.sent
        while c.next: c=c.next
        c.next=n
    def delete(self, v):
        c=self.sent
        while c.next:
            if c.next.val==v: c.next=c.next.next; return
            c=c.next
    def show(self):
        c,r=self.sent.next,[]
        while c: r.append(str(c.val)); c=c.next
        print(' -> '.join(r))
sl=SentinelList()
sl.append(10); sl.append(20); sl.append(30)
sl.push_front(5); sl.show(); sl.delete(10); sl.show()
