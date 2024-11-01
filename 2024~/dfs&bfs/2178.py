from collections import deque
import sys
input = sys.stdin.readline
# 1은 이동 가능, 0은 이동 불가능

def bfs(x, y):

    global graph, n, m
    dq = deque()
    dq.append((x, y))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))

    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

print(bfs(0,0))
