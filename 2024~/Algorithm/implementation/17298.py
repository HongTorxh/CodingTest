from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
result = [-1] * n
stack = deque()
for i in range(0, n-1):
    if arr[i] >= arr[i+1]:
         stack.append(i)
    else:
        for j in range(0,len(stack)):
            tmp = stack[-1]
            if arr[tmp] >= arr[i+1]:
                continue
            result[tmp] = arr[i+1]
            stack.pop()
        result[i] = arr[i+1]

for j in range(0,len(stack)):
    tmp = stack[-1]
    if arr[tmp] >= arr[-1]:
        continue
    result[tmp] = arr[-1]
    stack.pop()
    

answer = " ".join(str(i) for i in result)

print(answer)