# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

x = [10, 20, 30, 40]
s = x[1:3]
s is x
#   False
s[0] = 99
x
#   [10, 20, 30, 40]
s
#   [99, 30]
