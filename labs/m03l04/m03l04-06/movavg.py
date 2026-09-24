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
    def mean(self):
        s=[self.buf[(self.head+i)%self.cap] for i in range(self.size)]
        return sum(s)/len(s) if s else 0.0
rb=RingBuffer(3)
stream=[10,20,30,40,50]
for v in stream:
    rb.push(v)
    print(f'add {v}  mean={rb.mean():.1f}')
