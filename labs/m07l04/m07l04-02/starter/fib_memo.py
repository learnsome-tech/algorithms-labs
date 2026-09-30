import functools

calls_naive = 0
def fib_naive(n):
    global calls_naive
    calls_naive += 1
    if n <= 1: return n
    return fib_naive(n-1) + fib_naive(n-2)
calls_memo = 0
@functools.lru_cache(maxsize=None)
def fib_memo(n):
    global calls_memo
    calls_memo += 1
    if n <= 1: return n
    return fib_memo(n-1) + fib_memo(n-2)

n = 20
val = fib_naive(n)
fib_memo(n)
print('fib(' + str(n) + ') =', val)
print('naive calls:', calls_naive)
print('memo calls:', calls_memo)
