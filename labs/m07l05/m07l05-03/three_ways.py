# Algorithms & Data Structures for Working Engineers — lesson m07l05 — Recognising The Pattern
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l05
# © LearnSome.tech
import functools

def coin_greedy(amount):
    result = 0
    for c in [25, 10, 5, 1]:
        result += amount // c; amount %= c
    return result

@functools.lru_cache(maxsize=None)
def coin_memo(amount):
    if amount == 0: return 0
    return 1 + min(coin_memo(amount-c) for c in [1,5,10,25] if c<=amount)

def coin_dp(amount):
    dp = [0] + [10**9]*amount
    for i in range(1, amount+1):
        dp[i] = 1+min(dp[i-c] for c in [1,5,10,25] if c<=i)
    return dp[amount]
for amt in [11, 30, 41]:
    g, m, d = coin_greedy(amt), coin_memo(amt), coin_dp(amt)
    ok = 'agree' if g == m == d else 'DIFFER'
    print(f'amount {amt}: {g} coins [{ok}]')
