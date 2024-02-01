import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)


# dp[i] : i번째 날까지 일했을 때의 최댓값
dp = [0 for i in range(n+1)] 

for i in range(n-1, -1, -1):
    if t[i] + i <= n:
        dp[i] = max(dp[i + t[i]] + p[i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])