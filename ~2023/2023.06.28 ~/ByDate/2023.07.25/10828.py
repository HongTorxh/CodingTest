import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    temp = input().split()
    if temp[0] == "push":
        arr.append(temp[1])
    elif temp[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif temp[0] == "size":
        print(len(arr))
    elif temp[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])
    
    