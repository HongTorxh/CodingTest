import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    dq = deque()

    arr.sort()
    for i in range(n // 2):
        dq.appendleft(arr[i])
        dq.append(arr[n-i-1])
    print(dq)
    result = max(abs(dq[n // 2] - dq[n // 2 - 1]), abs(dq[n // 2] - dq[n // 2 + 1]))
    print(result)

    