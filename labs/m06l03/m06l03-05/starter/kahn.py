from collections import deque
deps = {'compile': [], 'link': ['compile'],
        'test': ['compile'], 'package': ['link','test'],
        'deploy': ['package']}
fwd = {n: [] for n in deps}
indeg = {n: 0 for n in deps}
for n in deps:
    for pre in deps[n]:
        fwd[pre].append(n)
        indeg[n] += 1
q = deque(n for n in deps if indeg[n] == 0)
order = []
while q:
    n = q.popleft()
    order.append(n)
    for m in fwd[n]:
        indeg[m] -= 1
        if indeg[m] == 0:
            q.append(m)
print(order)
