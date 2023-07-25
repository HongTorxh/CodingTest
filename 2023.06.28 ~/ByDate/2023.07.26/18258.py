import sys
input = sys.stdin.readline

n = int(input())

queue = []
j = 0
for i in range(n):
    temp = input().split()
    if temp[0] == "push":
        queue.append(temp[1])   
    elif temp[0] == "pop":
        if len(queue) > j:
            print(queue[j])
            j += 1
        else:
            print(-1)
    elif temp[0] == "size":
        print(len(queue) - j)
    elif temp[0] == "empty":
        if len(queue) == j:
            print(1)
            j = 0
            queue = []
        else:
            print(0)
    elif temp[0] == "front":
        if len(queue) > j:
            print(queue[j])
        else: 
            print(-1)
    elif temp[0] == "back":
        if len(queue) > j:
            print(queue[-1])
        else:
            print(-1)