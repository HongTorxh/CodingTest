import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cleaner = []

for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            cleaner.append(i)

def spread():
    new_board = [[0] * c for i in range(r)]
    
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                amt = board[i][j] // 5
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        new_board[nx][ny] += amt
                        cnt += 1
                new_board[i][j] += board[i][j] - (amt *  cnt)
            elif board[i][j] == -1:
                new_board[i][j] = -1
    return new_board

def clean():
    top = cleaner[0]
    for i in range(top - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    for i in range(c - 1):
        board[0][i] = board[0][i + 1]
    for i in range(top):
        board[i][c - 1] = board[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
        board[top][i] = board[top][i - 1]
    board[top][1] = 0

    # 아래쪽 공기청정기 (시계 방향)
    bottom = cleaner[1]
    for i in range(bottom + 1, r - 1):
        board[i][0] = board[i + 1][0]
    for i in range(c - 1):
        board[r - 1][i] = board[r - 1][i + 1]
    for i in range(r - 1, bottom, -1):
        board[i][c - 1] = board[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        board[bottom][i] = board[bottom][i - 1]
    board[bottom][1] = 0


for _ in range(t):
    board = spread()
    clean()

result = sum(sum(i for i in row if i > 0) for row in board)

print(result)