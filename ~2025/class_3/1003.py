import sys
input = sys.stdin.readline

t = int(input())

dp = [None] * 41
dp[0], dp[1] = (1, 0), (0,1)
for i in range(2, 41):
    a1, b1 = dp[i-1]
    a2, b2 = dp[i-2]
    dp[i] = (a1+a2, b1+b2)

for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])