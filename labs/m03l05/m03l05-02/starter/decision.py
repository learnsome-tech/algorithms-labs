scenarios = [
    ('task queue',   'deque',  'FIFO, grows at both ends'),
    ('undo history', 'list',   'stack LIFO, random access'),
    ('stream log',   'ring',   'bounded, overwrites oldest'),
    ('lookup table', 'dict',   'keyed, not a sequence'),
    ('fixed buffer', 'array',  'typed, contiguous memory'),
]
print(f'{"Scenario":<16} {"Structure":<10} Reason')
print('-'*60)
for scene,struct,reason in scenarios:
    print(f'{scene:<16} {struct:<10} {reason}')
