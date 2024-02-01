import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(t):
    f = int(input())
    for j in range(3, f+1):
        dp[j] = dp[j-3] + dp[j-2]
    print(dp[f-1])
