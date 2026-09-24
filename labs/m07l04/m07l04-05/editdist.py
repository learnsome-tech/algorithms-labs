# Algorithms & Data Structures for Working Engineers — lesson m07l04 — Dynamic Programming: Memoisation And Tabulation
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l04
# © LearnSome.tech
def edit_dist(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],
                                   dp[i][j-1],
                                   dp[i-1][j-1])
    return dp[m][n]

pairs = [('kitten', 'sitting'), ('sunday', 'saturday'), ('abc', 'abc')]
for a, b in pairs:
    print(f'edit_dist({a!r}, {b!r}) = {edit_dist(a, b)}')
