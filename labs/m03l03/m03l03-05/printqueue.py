# Algorithms & Data Structures for Working Engineers — lesson m03l03 — Stacks And Queues: Last In Or First In
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l03
# © LearnSome.tech
from collections import deque
jobs=deque()
def submit(job): jobs.append(job); print('queued:', job)
def process():
    if jobs: print('printing:', jobs.popleft())
    else: print('idle')
submit('report.pdf')
submit('slides.pdf')
submit('photo.jpg')
process()
process()
submit('invoice.pdf')
process()
process()
process()
