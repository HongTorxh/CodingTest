import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    result = 0
    while arr:
        maximum = max(arr)
        front = arr.popleft()
        m -= 1
        if maximum == front:
            result += 1
            if m < 0:
                print(result)
                break
        else:
            arr.append(front)
            if m < 0:
                m = len(arr) -1
            