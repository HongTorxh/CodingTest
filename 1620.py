import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dict = {}
for i in range(n):
    temp = input().rstrip()
    dict[temp] = 1

for j in range(m):
    temp = input().rstrip()
    if temp in dict:
        print(temp)
