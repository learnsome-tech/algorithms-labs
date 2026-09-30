import operator

records = [
    ('alice',  'eng', 85),
    ('bob',    'eng', 90),
    ('carol',  'mkt', 75),
    ('dave',   'mkt', 90),
    ('eve',    'eng', 85),
]

# stability composition: sort by secondary, then by primary
step1 = sorted(records, key=operator.itemgetter(1))
print('after dept sort:', [r[0] for r in step1])
step2 = sorted(step1, key=operator.itemgetter(2), reverse=True)
print('after score sort:', [r[0] for r in step2])
