# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

from collections import deque
w = deque(maxlen=4)
for v in [1,2,3,4]: w.append(v)
w
#   deque([1, 2, 3, 4], maxlen=4)
w.append(5)
w
#   deque([2, 3, 4, 5], maxlen=4)
w.append(6)
w
#   deque([3, 4, 5, 6], maxlen=4)
