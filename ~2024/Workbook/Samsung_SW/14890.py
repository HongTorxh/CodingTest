import sys

input = sys.stdin.readline

# 경사로의 높이는 항상 1, 길이는 L
# 경사로를 놓을 수 있으려면, 중복된 경사로면 안되고, 높이차가 1이여야 하며 L개가 연속되어야 하며, 범위를 벗어나면 안댐

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def is_valid(line, n, l):
    
    used = [False] * n

    for i in range(n-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i] - line[i+1]) == 1:
            # 높이가 낮아지는 경우
            if line[i] > line[i+1]:
                # 낮아졌으므로 i+1부터 쭉 l만큼의 길이가 확보되어있는지, 끝은 아닌지 확인
                for j in range(i+1, i+1+l):
                    if j >= n or line[j] != line[i+1] or used[j]:
                        return False
                    used[j] = True
            else:
                # 높아졌으므로 i부터 뒤로 쭉 l만큼의 길이가 확보되어있는지, 끝은 아닌지 확인
                for j in range(i, i - l, -1):
                    if j < 0 or line[j] != line[i] or used[j]:
                        return False
                    used[j] = True
        # 차이가 1이 아니면 경사로 조차를 만들 수 없음
        else:
            return False
    
    return True


result = 0
# 행 먼저
for row in board:   
    if is_valid(row, n, l):
        result += 1

for column in zip(*board):
    if is_valid(column, n, l):
        result += 1

print(result)
