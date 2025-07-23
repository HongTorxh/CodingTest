import sys
from collections import defaultdict
input = sys.stdin.readline

# n * n
# 학생 수 n^2

n = int(input())
board = [[0] * n for _ in range(n)]
students = []
likes = defaultdict(list)

for i in range(n*n):
    data = list(map(int, input().split()))
    students.append(data[0])
    likes[data[0]] = data[1:]


move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for student in students:
    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리 정하기
    # 좋아하는 학생 수가 몇명이나 자리에 앉았는지 count
    candidates = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                like_cnt = 0
                empty_cnt = 0
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in likes[student]:
                            like_cnt += 1
                        elif board[nx][ny] == 0:
                            empty_cnt += 1
                candidates.append((like_cnt, empty_cnt, x, y))

    candidates.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    
    _, _, x, y = candidates[0]
    board[x][y] = student

result = 0
for x in range(n):
    for y in range(n):
        student = board[x][y]
        like_cnt = 0
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in likes[student]:
                like_cnt += 1
        if like_cnt > 0:
            result += 10 ** (like_cnt - 1)

print(result)