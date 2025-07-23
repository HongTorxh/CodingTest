import sys

input = sys.stdin.readline

def spread(board, dusts):
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    global r, c
    # 1. 인접한 4방향으로 확산
    new_board = [[0] * c for _ in range(r)]
    for x, y in dusts:
        spread_amt = board[x][y] // 5
        spread_cnt = 0
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                new_board[nx][ny] += spread_amt
                spread_cnt += 1
        new_board[x][y] += board[x][y] - (spread_amt * spread_cnt)
    return new_board
def air_operation(board, air):
    
    global r, c
    # 아래쪽 먼저
    down = air[1]

    for i in range(down + 1, r - 1):
        board[i][0] = board[i+1][0]
        board[i+1][0] = 0
    for i in range(c-1):
        board[r-1][i] = board[r-1][i+1]
        board[r-1][i+1] = 0
    for i in range(r-1, down, -1):
        board[i][c-1] = board[i-1][c-1]
    for i in range(c-1, 1, -1):
        board[down][i] = board[down][i-1]
        board[down][i-1] = 0
    board[down][1] = 0
    #위쪽도
    up = air[0]

    for i in range(up - 1, 0, -1):
        board[i][0] = board[i-1][0]
        board[i-1][0] = 0
    for i in range(c-1):
        board[0][i] = board[0][i+1]
        board[0][i+1] = 0
    for i in range(up):
        board[i][c-1] = board[i+1][c-1]
        board[i+1][c-1] = 0
    for i in range(c-1, 1, -1):
        board[up][i] = board[up][i-1]
        board[up][i-1] = 0
    board[up][1] = 0
    



r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
air = []
dusts = []
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            air.append(i)
        elif board[i][j] > 0:
            dusts.append((i,j))  



for _ in range(t):
    board = spread(board, dusts)
    board[air[0]][0] = -1
    board[air[1]][0] = -1
    
    air_operation(board, air)
    dusts = [(i, j) for i in range(r) for j in range(c) if board[i][j] > 0]
    
print(sum(sum(cell for cell in row if cell > 0) for row in board))
