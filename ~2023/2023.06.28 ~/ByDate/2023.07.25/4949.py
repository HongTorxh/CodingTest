import sys
input = sys.stdin.readline

while(1):
    temp = input()
    if(temp[:-1] == "."):
        break
    stack = []
    flag = 0
    for j in temp[:-1]:
        if j == "(":
            stack.append(1)
        elif j == "[":
            stack.append(2)
        elif j == ")":
            if(len(stack) == 0 or stack[len(stack) -1] == 2):
                flag = 1
                break
            else:
                stack.pop()
        elif j == "]":
            if(len(stack) == 0 or stack[len(stack) -1] == 1):
                flag = 1
                break
            else:
                stack.pop()
    if(len(stack) == 0 and flag == 0):
        print("yes")
    else:
        print("no")
