roads = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('B', 1), ('D', 8)],
    'D': [],
}

for city, links in roads.items():
    for dest, cost in links:
        print(city, '->', dest, 'weight', cost)

print('directed edges:', sum(len(v) for v in roads.values()))
