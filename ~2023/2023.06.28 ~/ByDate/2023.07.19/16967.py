import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())

b = [list(map(int, input().split())) for i in range(h+x)] 

a = [[0 for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        a[i][j] = b[i][j]

for i in range(x, h):
    for j in range(y, w):
        a[i][j] = b[i][j] - a[i-x][j-y]

for i in range(h):
    for j in range(w):
        print(a[i][j], end = " ")
    print()
    

