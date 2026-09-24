# Algorithms & Data Structures for Working Engineers — lesson m06l01 — Representing A Graph: Matrix Or Adjacency List
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l01
# © LearnSome.tech
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
