import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        arr.pop()
    else:
        arr.append(temp)

print(sum(arr))