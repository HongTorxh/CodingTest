# 미로 탈출
# n * m 직사각형, 괴물을 피해 탈출
# 시작 위치 (1,1) 출구 (N,M)
# 괴물은 0, 없으면 1
# 탈출을 위해 움직여야 하는 최소 칸의 수
# [입력 조건]
# 첫째 줄 : N, M (4 <= N,M 200)
# 둘째 중 : N*M 행렬
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global n, m, graph
    dq = deque()
    dq.append((x,y))
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
                dq.append((nx,ny))
    return graph[n-1][m-1]

                

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

answer = bfs(0, 0)
print(answer)