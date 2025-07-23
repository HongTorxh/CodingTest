import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
# dp[i] : i개의 카드를 구매할 때 최솟값
# dp[i-j] + arr[j] : i-j번째 최솟값 + j개 카드팩의 값

dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i-j] + arr[j])

print(dp[n])
