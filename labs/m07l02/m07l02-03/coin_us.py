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

result = coin_greedy([1, 5, 10, 25], 41)
print('coins used:', result)
print('total:', len(result), 'coins')
