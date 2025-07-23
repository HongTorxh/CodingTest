import sys

input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
stack = []
tmp = 1
result = 0

for i, char in enumerate(arr):
    if char == "(":
        stack.append(char)
        tmp *= 2
    elif char == "[":
        stack.append(char)
        tmp *= 3
    elif char == ")":
        if not stack or stack[-1] != "(":
            print(0)
            sys.exit()
        if arr[i - 1] == "(":
            result += tmp
        stack.pop()
        tmp //= 2
    elif char == ']':
            if not stack or stack[-1] != '[':
                print(0)
                sys.exit()  # 올바르지 않은 괄호열
            if arr[i - 1] == '[':
                result += tmp
            stack.pop()
            tmp //= 3
    
print(result if not stack else 0)
    