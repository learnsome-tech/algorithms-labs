# Algorithms & Data Structures for Working Engineers — lesson m03l04 — Deques And Ring Buffers
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l04
# © LearnSome.tech
class RingBuffer:
    def __init__(self, cap):
        self.buf=[None]*cap
        self.cap=cap
        self.head=0
        self.tail=0
        self.size=0
    def push(self, v):
        if self.size==self.cap:
            self.head=(self.head+1)%self.cap
        else:
            self.size+=1
        self.buf[self.tail]=v
        self.tail=(self.tail+1)%self.cap
    def items(self):
        return [self.buf[(self.head+i)%self.cap] for i in range(self.size)]
rb=RingBuffer(4)
for v in [10,20,30,40]: rb.push(v)
print(rb.items())
rb.push(50)
print(rb.items())
rb.push(60); print(rb.items())
