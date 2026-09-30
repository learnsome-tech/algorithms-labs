import heapq

def huffman(freq):
    nodes = sorted(freq.items())
    heap = [(w, i, s, None, None) for i,(s,w) in enumerate(nodes)]
    heapq.heapify(heap)
    idx = len(heap)
    while len(heap) > 1:
        w1,_,s1,l1,r1 = heapq.heappop(heap)
        w2,_,s2,l2,r2 = heapq.heappop(heap)
        heapq.heappush(heap,(w1+w2,idx,None,
            (w1,0,s1,l1,r1),(w2,0,s2,l2,r2)))
        idx += 1
    def depth(node, d=0):
        w,_,s,l,r = node
        if s: yield s, d
        if l: yield from depth(l, d+1)
        if r: yield from depth(r, d+1)
    return dict(depth(heap[0]))
freq = {'a':45,'b':13,'c':12,'d':16,'e':9,'f':5}
for sym, bits in sorted(huffman(freq).items()):
    print(sym, bits)
