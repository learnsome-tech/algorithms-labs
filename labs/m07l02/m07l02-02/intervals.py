# Algorithms & Data Structures for Working Engineers — lesson m07l02 — Greedy Algorithms: When Local Is Global
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l02
# © LearnSome.tech
def schedule(intervals):
    chosen = []
    intervals.sort(key=lambda iv: iv[1])
    last_end = float('-inf')
    for start, end in intervals:
        if start >= last_end:
            chosen.append((start, end))
            last_end = end
    return chosen

meetings = [(0,6),(1,4),(3,5),(3,8),(4,7),(5,9),(6,10),(8,11)]
result = schedule(meetings)
for s, e in result:
    print(s, 'to', e)
print('total chosen:', len(result))
