import sys, math
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
arr = [i*i for i in range(1, int(math.sqrt(n)) + 1)]

for i in range(1, n+1):
    for j in arr:
        if j > i:
            break
        dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[n])