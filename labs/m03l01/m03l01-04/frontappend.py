# Algorithms & Data Structures for Working Engineers — lesson m03l01 — Arrays: Contiguous Memory And Constant-Time Access
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l01
# © LearnSome.tech
n=10000
front_moves=sum(range(n))
append_ops=n
print('inserting at front,', n, 'calls:', front_moves, 'shifts')
print('appending,', n, 'calls:', append_ops, 'ops')
print('front insert is costlier:', front_moves > append_ops)
