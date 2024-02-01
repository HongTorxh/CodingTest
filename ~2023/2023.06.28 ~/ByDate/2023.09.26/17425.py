import sys
input = sys.stdin.readline

t = int(input())
MAX = 1000001
dp = [0] * MAX
dp[0] = 0
prefixSum = [0] * MAX
for i in range(1,MAX):
    j = 1
    while i*j < MAX:
        dp[i*j] += i
        j += 1
    prefixSum[i] = prefixSum[i-1] + dp[i]


for i in range(t):
    n = int(input())
    print(prefixSum[n])
    