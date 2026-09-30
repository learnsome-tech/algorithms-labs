# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

d = {'b': 2, 'a': 1, 'c': 3}
list(d.keys())
#   ['b', 'a', 'c']
d['d'] = 4
list(d.keys())
#   ['b', 'a', 'c', 'd']
9999 in list(range(10000))
#   True
9999 in set(range(10000))
#   True
(3, 4) in {(1, 2), (3, 4)}
#   True
