# Algorithms & Data Structures for Working Engineers — lesson m07l02 — Greedy Algorithms: When Local Is Global
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l02
# © LearnSome.tech
def coin_greedy(coins, amount):
    coins = sorted(coins, reverse=True)
    used = []
    for c in coins:
        while amount >= c:
            used.append(c)
            amount -= c
    return used

def coin_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i-c]+1 < dp[i]:
                dp[i] = dp[i-c] + 1
    return dp[amount]

coins, amount = [1, 3, 4], 6
g = coin_greedy(coins, amount)
print('greedy:', g, 'coins used:', len(g))
print('optimal count:', coin_dp(coins, amount))
