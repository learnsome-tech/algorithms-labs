# Algorithms & Data Structures for Working Engineers — lesson m02l03 — Python Dicts And Sets Under The Hood
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l03
# © LearnSome.tech
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

p1, p2 = Point(3, 4), Point(3, 4)
print(p1 == p2)
print(hash(p1) == hash(p2))
s = {p1}
print(p2 in s)
d = {p1: 'origin'}
print(d[p2])
