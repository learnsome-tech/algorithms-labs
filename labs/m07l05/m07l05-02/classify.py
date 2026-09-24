# Algorithms & Data Structures for Working Engineers — lesson m07l05 — Recognising The Pattern
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l05
# © LearnSome.tech
RULES = {
    'overlapping subproblems': 'dynamic programming',
    'greedy choice holds':     'greedy algorithm',
    'need all solutions':      'backtracking',
    'solutions merge':         'divide and conquer',
}

problems = [
    ('weighted shortest path', 'greedy choice holds'),
    ('count arrangements',     'need all solutions'),
    ('common subsequence',     'overlapping subproblems'),
    ('sort by comparison',     'solutions merge'),
]

for name, trait in problems:
    print(f'{name}: {RULES[trait]}')
