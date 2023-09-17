import sys
input = sys.stdin.readline
from collections import deque

def dfs(matrix, i, visited):
    visited[i] = True
    print(i, end=' ')
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1 and not visited[j]:
            dfs(matrix, j, visited)

def bfs(matrix, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for c in range(len(matrix[value])):
        if matrix[value][c] == 1 and not visited[c]:
          queue.append(c)


n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n + 1)
# print(arr)

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


dfs(matrix, v, visited)
print()
bfs(matrix, v, visited)