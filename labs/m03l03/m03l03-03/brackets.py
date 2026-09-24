# Algorithms & Data Structures for Working Engineers — lesson m03l03 — Stacks And Queues: Last In Or First In
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l03
# © LearnSome.tech
def balanced(s):
    stack=[]
    pairs={'(':')','[':']','{':'}'}
    for c in s:
        if c in pairs:
            stack.append(c)
        elif c in pairs.values():
            if not stack or pairs[stack[-1]]!=c:
                return False
            stack.pop()
    return len(stack)==0

tests=['(a+b)*(c-d)','[1,{2,3}]','((open','([)]']
for t in tests:
    print(t, '->', balanced(t))
