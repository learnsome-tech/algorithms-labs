# Algorithms & Data Structures for Working Engineers — lesson m03l03 — Stacks And Queues: Last In Or First In
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

stack = []
stack.append('a')
stack
#   ['a']
stack.append('b')
stack.append('c')
stack
#   ['a', 'b', 'c']
stack.pop()
#   'c'
stack
#   ['a', 'b']
