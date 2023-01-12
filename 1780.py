import sys
input = sys.stdin.readline

def check(x, y, n):
    global pluspaper, zeropaper, minuspaper
    temp = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if temp != arr[i][j]:
                check(x, y, n//3)
                check(x + n//3, y, n//3)
                check(x + (n//3 * 2), y , n//3)
                check(x, y+n//3, n//3)
                check(x, y + (n//3 *2), n//3)
                check(x + n//3, y + n//3 , n//3)
                check(x + (n//3*2), y + n//3, n//3)
                check(x + n//3, y + (n//3*2), n//3)
                check(x + (n//3*2) , y + (n//3* 2), n//3)
                return
    if temp == -1:
        minuspaper += 1
    elif temp == 0:
        zeropaper += 1
    else:
        pluspaper += 1



n = int(input())
arr = [list(map(int, input().split())) for _ in range(0, n)]
pluspaper = 0
zeropaper = 0 
minuspaper = 0


check(0, 0, n)

print(minuspaper)
print(zeropaper)
print(pluspaper)