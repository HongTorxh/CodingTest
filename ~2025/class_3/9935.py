import sys

input = sys.stdin.readline

s = input().strip()
bomb = input().strip()

stack = []
for ch in s:
    stack.append(ch)
    if len(stack) >= len(bomb):
        if stack[-len(bomb): ] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()

print(''.join(stack) if len(stack) != 0 else "FRULA")

