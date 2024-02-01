import sys
input = sys.stdin.readline
n, m = map(int, input().split())


dict = {}
for i in range(1,n+1):
    temp = input().rstrip()
    dict[temp] = str(i)
    dict[str(i)] = temp 
for i in range(m):
    temp = input().rstrip()
    print(dict[temp])