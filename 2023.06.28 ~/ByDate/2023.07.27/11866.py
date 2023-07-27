import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

arr = deque([i for i in range(1, N+1)])

result = []
for i in range(N):
    arr.rotate(-K)
    result.append(arr.pop())

print("<", end= "")
for i in range(N):
    if(i == N-1):
        print(result[i], end = "")
        break
    print(result[i], end="")
    print(", ", end = "")
print(">", end="")