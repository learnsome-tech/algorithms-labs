def sift_up(h, i):
    while i > 0:
        p = (i - 1) // 2
        if h[p] > h[i]: h[p], h[i] = h[i], h[p]; i = p
        else: break

def sift_down(h, i, n):
    while True:
        l, r, s = 2*i+1, 2*i+2, i
        if l < n and h[l] < h[s]: s = l
        if r < n and h[r] < h[s]: s = r
        if s == i: break
        h[i], h[s] = h[s], h[i]; i = s

h = []
for v in [5, 3, 8, 1, 4]:
    h.append(v); sift_up(h, len(h) - 1)
print('min-heap array:', h)
v = h[0]; h[0] = h[-1]; h.pop(); sift_down(h, 0, len(h))
print('extracted minimum:', v)
print('heap after extraction:', h)
