from collections import deque
G = {'Alice': ['Bob','Carol'], 'Bob': ['Alice','Dave'],
     'Carol': ['Alice','Dave'], 'Dave': ['Bob','Carol']}
def bfs_path(G, src, dst):
    parent = {src: None}
    q = deque([src])
    while q:
        u = q.popleft()
        if u == dst:
            break
        for v in G[u]:
            if v not in parent:
                parent[v] = u
                q.append(v)
    path, node = [], dst
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))
print(bfs_path(G, 'Alice', 'Dave'))
