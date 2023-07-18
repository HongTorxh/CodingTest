import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque([i for i in range(1, n+1)])

if(n == 1):
    print(deq[0])

else:
    while(1):
        deq.popleft()
        if(len(deq) == 1):
            break
        deq.append(deq[0])
        deq.popleft()
    print(deq[0])    

