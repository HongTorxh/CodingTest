import sys, itertools

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

answer = float('inf')
visited = [False] * n

def dfs(start, idx, s, cnt):
    global answer
    if cnt == n:
        if arr[idx][start] != 0:
            s += arr[idx][start]
            answer = min(answer, s)
        return
    if s > answer:
        return
    
    for i in range(n):
        if not visited[i] and arr[idx][i] != 0:
            visited[i] = True
            dfs(start, i, s + arr[idx][i], cnt + 1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(answer)
        