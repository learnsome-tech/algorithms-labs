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
