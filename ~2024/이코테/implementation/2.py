# 왕실의 나이트
# 8*8 체스판
# 2가지 이동 방법
# 1. 수평 2칸 이동 수직 1칸 이동
# 2. 수직 2칸 이동 수평 1칸 이동
# 행 위는 a ~ h로, 열은 1~8로
# [입력 조건]
# 현재 나이트의 위치를 보여줌
# 나이트가 이동할 수 있는 경우의 수 출력

import sys
input = sys.stdin.readline

arr = list(map(str, (i for i in input().rstrip())))
moves = [[-2, -1], [-2, 1], [2, -1], [2, 1], [1,-2], [1,2], [-1, -2], [-1,2]]
answer = 0
arr[0] = ord(arr[0]) - 97 + 1
arr[1] = int(arr[1])
for move in moves:
    nx = arr[0] + move[0]
    ny = arr[1] + move[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        answer += 1

print(answer)