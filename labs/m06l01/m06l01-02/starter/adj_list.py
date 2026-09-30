graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['B'],
}

for node, neighbours in graph.items():
    print(node, '->', neighbours)

edges = sum(len(v) for v in graph.values()) // 2
print('edges:', edges)
