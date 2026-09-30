import heapq

chunks = [
    [12, 35, 67, 89],
    [3, 24, 56, 91],
    [18, 42, 55, 78],
]
for i, chunk in enumerate(chunks):
    with open(f'chunk{i}.txt', 'w') as f:
        for v in chunk:
            f.write(f'{v}\n')

handles = [open(f'chunk{i}.txt') for i in range(3)]
merged = list(heapq.merge(*(map(int, h) for h in handles)))
for h in handles: h.close()
print('merged:', merged)
print('verified:', merged == sorted(sum(chunks, [])))
