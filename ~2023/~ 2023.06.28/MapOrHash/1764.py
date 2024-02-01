import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dict = {}
for i in range(n):
    temp = input().rstrip()
    dict[temp] = 1

arr = []

for j in range(m):
    temp = input().rstrip()
    if temp in dict:
        arr.append(temp)

arr.sort()
print(len(arr))
for item in arr:
    print(item)
