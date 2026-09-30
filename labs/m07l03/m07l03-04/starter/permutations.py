def perms(items):
    if len(items) <= 1:
        yield tuple(items)
        return
    for i, v in enumerate(items):
        rest = items[:i] + items[i+1:]
        for p in perms(rest):
            yield (v,) + p

result = list(perms([1, 2, 3, 4]))
print('count:', len(result))
for p in result[:4]:
    print(' ', p)
