import sys
input = sys.stdin.readline

# N인 정사각형

n = int(input())
arr = [list(map(str, input().strip())) for _ in range(n)]
# [심장 x, 심장 y, 왼팔, 오른팔, 허리, 왼다리, 오른 다리]
result = [0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    flag = False
    for j in range(n):
        if arr[i][j] == "*":
            result[0] = i+1
            result[1] = j
            flag = True
            break
    if flag:
        break

# 왼팔
for i in range(result[1] - 1, -1, -1):
    if arr[result[0]][i] != '*':
        break
    result[2] += 1
# 오른팔
for i in range(result[1] + 1, n):
    if arr[result[0]][i] != '*':
        break
    result[3] += 1
# 허리
for i in range(result[0] + 1, n):
    if arr[i][result[1]] != '*':
        break
    result[4] += 1
# 왼다리
for i in range(result[0] + 1 + result[4], n):
    if arr[i][result[1] - 1] != '*':
        break
    result[5] += 1
for i in range(result[0] + 1 + result[4], n):
    if arr[i][result[1] + 1] != '*':
        break
    result[6] += 1

print(result[0] + 1, result[1] + 1)
print(" ".join(str(result[i]) for i in range(2, 7)))