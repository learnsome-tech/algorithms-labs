# Algorithms & Data Structures for Working Engineers — lesson m05l04 — B-Trees: The Structure Behind Every Database Index
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l04
# © LearnSome.tech
import math
n = 1_000_000
t = 512
fanout = 2 * t
levels = math.ceil(math.log(n + 1, fanout))
print('fanout with t equal to', t, 'is', fanout)
print('levels for a million keys:', levels)
print('disk reads for any search:', levels)
