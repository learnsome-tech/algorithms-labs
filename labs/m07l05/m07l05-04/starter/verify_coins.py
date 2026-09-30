def coin_greedy(amount):
    result = 0
    for c in [25, 10, 5, 1]:
        result += amount // c; amount %= c
    return result

def coin_dp(amount):
    dp = [0] + [10**9]*amount
    for i in range(1, amount+1):
        dp[i] = 1+min(dp[i-c] for c in [1,5,10,25] if c<=i)
    return dp[amount]

mismatches = 0
for amount in range(1, 100):
    if coin_greedy(amount) != coin_dp(amount):
        mismatches += 1
        print('mismatch at', amount)
print('tested one to ninety-nine')
print('mismatches found:', mismatches)
