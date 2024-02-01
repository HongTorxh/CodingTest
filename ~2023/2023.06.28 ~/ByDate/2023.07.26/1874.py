import sys
input = sys.stdin.readline

def push(num):
    global stack,result, j
    for k in range(j, num+1):
        stack.append(k)
        result.append("+")
    j = num+1

def pop(num):
    global stack, result, flag
    if num == stack[len(stack)-1]:
        stack.pop()
        result.append("-")
    else:
        flag = 1

n = int(input())

stack = []
result = []
flag = 0

j = 1
for i in range(n):
    temp = int(input())
    if temp < j:
        pop(temp)
    else:
        push(temp)
        pop(temp)
    
if flag == 1:
    print("NO")
else:
    for i in result:
        print(i)