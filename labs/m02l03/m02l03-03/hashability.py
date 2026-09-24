# Algorithms & Data Structures for Working Engineers — lesson m02l03 — Python Dicts And Sets Under The Hood
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l03
# © LearnSome.tech
try:
    hash([1, 2, 3])
except TypeError as e:
    print(e)
print('tuple is hashable:', hash((1, 2, 3)) == hash((1, 2, 3)))
