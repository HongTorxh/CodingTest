import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for i in range(t):
    func = input()
    l = int(input())
    # tmp = list(map(int, input().strip().strip('[]').split(',')))
    tmp = list(map(str, input().strip().strip('[]').split(',')))
    if tmp[0] == '':
        tmp.pop()
    tmp = list(map(int, tmp))
    arr = deque(tmp)
    flag = 0
    is_reversed = False
    for j in func:
        if j == 'R':
            is_reversed = not is_reversed
        elif j == 'D':
            if arr:
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()
    if is_reversed:
        arr.reverse()
    print(list(arr))