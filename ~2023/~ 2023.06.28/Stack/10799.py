import sys
input = sys.stdin.readline

arr = list(input())
stack = []
result = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    else:
        if arr[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
            

print(result)