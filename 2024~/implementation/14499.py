import sys
input = sys.stdin.readline

n, m, x, y, k = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

commands = list(map(int, input().split()))

move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

dice = [0] * 7
floor = 6
top = 1
# (1,6), (2,5), (3, 4)

for command in commands:
    dx, dy = move[command - 1]
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    ### 방향에 따라 주사위 굴리기~~~!!
    if command == 1:
        # [1,2,3,4,5,6] => [4, 2, 1, 6, 5, 3]
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif command == 2:
        # [1,2,3,4,5,6] => [3,2,6,1,5,4]
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif command == 3:
        # [1,2,3,4,5,6] => [5,1,3,4,6,2]
        dice[1],dice[2],dice[5],dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif command == 4:
        # [1,2,3,4,5,6] => [2,6,3,4,1,5]
        dice[1], dice[2],dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


    if board[nx][ny] == 0:
        board[nx][ny] = dice[6]
    else:
        dice[6] = board[nx][ny]
        board[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[1])