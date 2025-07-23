import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
result = [1] * N
for i in range(N):
    x, y = arr[i]
    for j in range(N):
        nx, ny = arr[j]
        if i == j:
            continue
        if nx > x and ny > y:
            result[i] += 1

print(*result)