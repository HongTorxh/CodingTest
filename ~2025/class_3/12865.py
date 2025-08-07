# 2025.08.07 2
# 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n개의 물건, 버틸 수 있는 무게 k
# [w, v] = 무게, 가치
arr = [list(map(int, input().split())) for _ in range(n)]
# dp[i][w] = i번째 물건을 선택했을 때, 무게 w이면서 가치
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, k+1):
        if arr[i-1][0] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - arr[i-1][0]] + arr[i-1][1])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])