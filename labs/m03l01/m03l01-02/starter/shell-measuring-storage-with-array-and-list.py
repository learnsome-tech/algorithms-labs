# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import array, sys
a = array.array('i', range(100))
sys.getsizeof(a)
#   488
b = list(range(100))
sys.getsizeof(b)
#   856
sys.getsizeof(a) < sys.getsizeof(b)
#   True
