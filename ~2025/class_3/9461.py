import sys
input = sys.stdin.readline

t = int(input())

dp = [1] * 101

for i in range(3, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    print(dp[int(input()) - 1])