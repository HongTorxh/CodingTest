# 2025.07.24 5
# 경로 찾기
import sys
input = sys.stdin.readline

n = int(input()) #정점 수
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(*row)