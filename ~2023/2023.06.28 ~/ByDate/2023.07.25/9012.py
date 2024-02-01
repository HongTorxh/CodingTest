import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    temp = input()
    stack = []
    flag = 0
    for j in temp[:-1]:
        if j == "(":
            stack.append(1)
        else:
            if(len(stack) == 0):
                flag = 1
                break
            else:
                stack.pop()
    if(len(stack) == 0 and flag == 0):
        print("YES")
    else:
        print("NO")
