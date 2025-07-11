import sys
input = sys.stdin.readline

def divide(x, y, m):
    global white, blue
    start = board[x][y]
    if m == 1:
        if start == 0:
            white += 1
            return
        else:
            blue += 1
            return
    for i in range(x, x + m):
        for j in range(y, y + m):
            if board[i][j] != start:
                divide(x, y, m // 2) # 0, 0
                divide(x + m // 2, y, m // 2) # 4, 0
                divide(x , y + m // 2, m // 2) # 0, 4
                divide(x + m // 2, y + m // 2, m // 2) # # 4, 4
                return
    if start == 0:
        white += 1
    else:
        blue += 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0 #white = 0 / blue = 1

divide(0, 0, n)

print(white, blue)