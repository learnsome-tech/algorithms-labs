# Algorithms & Data Structures for Working Engineers — lesson m05l05 — Heaps And Priority Queues
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m05l05
# © LearnSome.tech
import heapq

tasks = []
heapq.heappush(tasks, (3, 'deploy database'))
heapq.heappush(tasks, (1, 'page on-call engineer'))
heapq.heappush(tasks, (2, 'notify team'))
heapq.heappush(tasks, (1, 'open incident channel'))

print('processing in priority order:')
while tasks:
    pri, name = heapq.heappop(tasks)
    print(' priority', pri, ':', name)
