import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs (i, j, board):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dq = deque([(i, j)])

    while dq:
        x, y = dq.popleft()
        board[x][y] = 0
        for dx,dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = 0
                dq.append((nx,ny))

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(i, j, board)
                result += 1
    print(result)
