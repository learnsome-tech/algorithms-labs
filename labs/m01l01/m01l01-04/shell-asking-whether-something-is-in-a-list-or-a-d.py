# Algorithms & Data Structures for Working Engineers — lesson m01l01 — Why Complexity Matters In Production
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

users_list = ['alice', 'bob', 'carol']
users_dict = {'alice': 1, 'bob': 2, 'carol': 3}
'alice' in users_list
#   True
'alice' in users_dict
#   True
'zara' in users_list
#   False
'zara' in users_dict
#   False
