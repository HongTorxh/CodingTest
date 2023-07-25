import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(n):
    temp = input()
    if(len(temp[:-1]) < m):
        continue
    else:
        if temp[:-1] in dict:
            dict[temp[:-1]] += 1
        else:
            dict[temp[:-1]] = 1

dict = sorted(dict.items(), key = lambda x: (-x[1],-len(x[0]), x[0]))

for i in dict:
    print(i[0])
