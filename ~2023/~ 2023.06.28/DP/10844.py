import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for i in range(101)]

dp[1][0] = 0
for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

result = 0
for i in range(0,10):
    # print(dp[n][i])
    result = (result + dp[n][i]) % 1000000000
    

print(dp[3][4])
print(result)

# Dynamic Programming 
# dp[n][i]에서 n은 input에 대한 단계와 끝자리 숫자는 배열의 index를 의미한다. 즉, 끝자리 숫자를 기준으로 dp[2][0]은 길이가 2인 n이라는 숫자중에 0으로 끝나는 숫자는 10으로 1개이기 때문에 1이다. dp[2][2]는 12, 32로 두가지이기 떄문에 2가 저장됨. 