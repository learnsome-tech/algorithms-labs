employees = [
    ('alice', 'eng', 85),
    ('bob',   'mkt', 90),
    ('carol', 'eng', 90),
    ('dave',  'mkt', 85),
    ('eve',   'eng', 85),
]

# dept asc, then score desc, then name asc
result = sorted(employees, key=lambda e: (e[1], -e[2], e[0]))
print('dept asc, score desc, name asc:')
for name, dept, score in result:
    print(f'  {name:<8} {dept:<4} {score}')
