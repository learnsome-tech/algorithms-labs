# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

from collections import deque
q = deque(['Alice'])
q.append('Bob')
q.append('Carol')
q.popleft()
#   'Alice'
q.popleft()
#   'Bob'
q
#   deque(['Carol'])
