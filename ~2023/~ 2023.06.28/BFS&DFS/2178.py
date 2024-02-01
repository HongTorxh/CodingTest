def dfs():
    if

n, m = map(int, input().split())

arr = [[0 for i in range(m)] for i in range(n)]

j = 0
for i in range(n):
    a = int(input())
    k = m-1
    for i in range(m):
        arr[j][k] = a % 10
        a = a // 10
        k = k - 1
    j += 1

