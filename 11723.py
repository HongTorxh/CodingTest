import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    temp = input().split()
    if temp[0] == 'add':
        if temp[1] in arr:
            continue
        else:
            arr.append(temp[1])
    elif temp[0] == 'remove':
        if temp[1] not in arr:
            continue
        else:
            arr.remove(temp[1])
    elif temp[0] == 'check':
        if temp[1] in arr:
            print(1)
        else:
            print(0)
    elif temp[0] == 'toggle':
        if temp[1] in arr:
            arr.remove(temp[1])
        else:
            arr.append(temp[1])
    elif temp[0] == 'all':
            arr = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    elif temp[0] == 'empty':
            arr = []
