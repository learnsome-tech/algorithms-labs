# Algorithms & Data Structures for Working Engineers — lesson m07l04 — Dynamic Programming: Memoisation And Tabulation
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l04
# © LearnSome.tech
def knapsack(weights, values, cap):
    n = len(weights)
    dp = [[0]*(cap+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(cap+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                take = dp[i-1][w-weights[i-1]] + values[i-1]
                if take > dp[i][w]:
                    dp[i][w] = take
    return dp

weights = [1, 2, 3]
values  = [1, 4, 3]
cap = 4
dp = knapsack(weights, values, cap)
header = '     ' + '  '.join(str(w) for w in range(cap+1))
print(header)
for i, row in enumerate(dp):
    print(f'[{i}]  ' + '  '.join(str(v) for v in row))
print('max value:', dp[len(weights)][cap])
