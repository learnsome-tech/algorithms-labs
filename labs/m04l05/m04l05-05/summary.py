# Algorithms & Data Structures for Working Engineers — lesson m04l05 — Searching With Hashes Versus Trees
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l05
# © LearnSome.tech
print(f"{'operation':<20} {'set/dict':>10} {'sorted list':>13} {'linear':>8}")
print('-' * 53)
rows = [
    ('membership',    'O(1)',       'O(log n)',     'O(n)'),
    ('insert',        'O(1)',       'O(n)',         'O(n)'),
    ('delete',        'O(1)',       'O(n)',         'O(n)'),
    ('range query',   'O(n)',       'O(log n + k)', 'O(n)'),
    ('sorted walk',   'O(n log n)', 'O(n)',         'O(n)'),
]
for op, h, s, l in rows:
    print(f'{op:<20} {h:>10} {s:>13} {l:>8}')
