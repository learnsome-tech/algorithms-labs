G = {'A': ['B', 'C'], 'B': ['D', 'E'],
     'C': ['F'], 'D': [], 'E': ['F'], 'F': []}

def dfs(G, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print('visit', node)
    for nb in G[node]:
        if nb not in visited:
            dfs(G, nb, visited)

dfs(G, 'A')
