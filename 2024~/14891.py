import sys
from collections import deque
input = sys.stdin.readline

arr = []
for _ in range(4):
    arr.append(deque(list(map(int, input().rstrip()))))
    
k = int(input())


for _ in range(k):
    num, dir = map(int, input().split())
    # 1은 시계, -1은 반시계
    # 2 <-> 6 - 2 <-> 6 2 <-> 6
    if num == 1:
        if arr[0][2] == arr[1][6]:
            arr[0].rotate(dir)
        else: 
            arr[0].rotate(dir)
            dir = -dir
            if arr[1][2] == arr[2][6]:
                arr[1].rotate(dir)
            else:
                arr[1].rotate(dir)
                dir = -dir
                if arr[2][2] == arr[3][6]:
                    arr[2].rotate(dir)
                else:
                    arr[2].rotate(dir)
                    dir = -dir
                    arr[3].rotate(dir)
    elif num == 2:
        if arr[0][2] != arr[1][6]:
            arr[0].rotate(-dir)
        if arr[1][2] == arr[2][6]:
            arr[1].rotate(dir)
        else:
            arr[1].rotate(dir)
            dir = -dir
            if arr[2][2] == arr[3][6]:
                arr[2].rotate(dir)
            else:
                arr[2].rotate(dir)
                dir = -dir
                arr[3].rotate(dir)
    elif num == 3:
        if arr[3][6] != arr[2][2]:
            arr[3].rotate(-dir)
        if arr[2][6] == arr[1][2]:
            arr[2].rotate(dir)
        else:
            arr[2].rotate(dir)
            dir = -dir
            if arr[1][6] == arr[0][2]:
                arr[1].rotate(dir)
            else:
                arr[1].rotate(dir)
                dir = -dir
                arr[0].rotate(dir)
    else:
        if arr[3][6] == arr[2][2]:
            arr[3].rotate(dir)
        else:
            arr[3].rotate(dir)
            dir = -dir
            if arr[2][6] == arr[1][2]:
                arr[2].rotate(dir)
            else:
                arr[2].rotate(dir)
                dir = -dir
                if arr[1][6] == arr[0][2]:
                    arr[1].rotate(dir)
                else:
                    arr[1].rotate(dir)
                    dir = -dir
                    arr[0].rotate(dir)
answer = 0

if arr[0][0] == 1:
    answer += 1
if arr[1][0] == 1:
    answer += 2
if arr[2][0] == 1:
    answer += 4
if arr[3][0] == 1:
    answer += 8

print(answer)

