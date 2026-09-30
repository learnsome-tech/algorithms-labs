def iterative_sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print('sum of ten:', iterative_sum(10))
print('sum of two thousand:', iterative_sum(2000))
print('sum of one million:', iterative_sum(1000000))
