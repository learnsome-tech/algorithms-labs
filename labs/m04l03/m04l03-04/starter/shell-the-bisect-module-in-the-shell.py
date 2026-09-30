# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import bisect
a = [1, 3, 5, 7, 9]
bisect.bisect_left(a, 5)
#   2
bisect.bisect_left(a, 4)
#   2
bisect.bisect_right(a, 5)
#   3
bisect.insort(a, 6)
a
#   [1, 3, 5, 6, 7, 9]
