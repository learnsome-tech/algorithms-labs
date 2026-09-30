# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

order = ['compile','link','test','package','deploy']
order.index('compile')
#   0
order.index('package')
#   3
order.index('link') < order.index('package')
#   True
order.index('test') < order.index('package')
#   True
