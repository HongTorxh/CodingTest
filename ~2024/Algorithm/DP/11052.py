import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)



# dp[i] = 카드 i개를 구매할 때의 최댓값
# dp[i-j] + arr[j] = i-j개의 카드 선택 시의 최댓값 + j개 선택시 최댓값 
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + arr[j])

print(dp[n])