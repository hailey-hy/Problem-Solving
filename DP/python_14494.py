# 다이나믹이 뭐예요?

n, m = map(int, input().split())

dp = [[1] * m for i in range(n)]

total = 0

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]

print(dp[n - 1][m - 1] % 1000000007)