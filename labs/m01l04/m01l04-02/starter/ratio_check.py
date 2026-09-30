def linear_work(n):
    count = 0
    for i in range(n):
        count += 1
    return count

def quad_work(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

print('n       lin  lin/n  quad      quad/n')
for n in [100, 1000, 10000]:
    lin = linear_work(n)
    quad = quad_work(n)
    print(n, lin, lin // n, quad, quad // n)
