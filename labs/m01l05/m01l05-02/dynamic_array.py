# Algorithms & Data Structures for Working Engineers — lesson m01l05 — Amortised Analysis: Why Append Is Cheap
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l05
# © LearnSome.tech
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.length = 0
        self.total_copies = 0

    def append(self, value):
        if self.length == self.capacity:
            self.total_copies += self.length
            self.capacity *= 2
        self.length += 1

arr = DynamicArray()
for i in range(16):
    arr.append(i)
print('appended:', arr.length)
print('capacity:', arr.capacity)
print('total copies:', arr.total_copies)
print('average copies:', arr.total_copies / arr.length)
