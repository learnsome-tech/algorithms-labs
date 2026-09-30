import sys

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print('sum of ten:', recursive_sum(10))
print('recursion limit:', sys.getrecursionlimit())

try:
    recursive_sum(2000)
    print('two thousand: ok')
except RecursionError:
    print('two thousand: RecursionError')
