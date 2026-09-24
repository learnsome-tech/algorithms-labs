# Algorithms & Data Structures for Working Engineers — lesson m01l01 — Why Complexity Matters In Production
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l01
# © LearnSome.tech
def find_user(user_id, users):
    for u in users:
        if u == user_id:
            return True
    return False

users = ['alice', 'bob', 'carol', 'dave', 'eve']
print(find_user('carol', users))
print(find_user('zara', users))
