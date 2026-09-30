# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

words = ['banana', 'fig', 'apple', 'cherry']
sorted(words, key=len)
#   ['fig', 'apple', 'banana', 'cherry']
sorted(words, key=len, reverse=True)
#   ['banana', 'cherry', 'apple', 'fig']
import operator
data = [('alice', 85), ('bob', 90), ('carol', 85)]
sorted(data, key=operator.itemgetter(1))
#   [('alice', 85), ('carol', 85), ('bob', 90)]
sorted(data, key=operator.itemgetter(0))
#   [('alice', 85), ('bob', 90), ('carol', 85)]
