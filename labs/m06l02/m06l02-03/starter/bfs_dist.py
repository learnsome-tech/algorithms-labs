from collections import deque

G = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'Dave'],
    'Carol': ['Alice', 'Dave'],
    'Dave': ['Bob', 'Carol'],
}

def bfs(G, src):
    dist = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in G[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

for name, d in bfs(G, 'Alice').items():
    print(name, 'distance', d)
