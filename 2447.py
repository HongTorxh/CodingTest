import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def paint(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            paint(x, y, n//3)
            paint(x+n//3, y, n//3)
            paint(x, y+n//3, n//3)
            paint(x+n//3, y+n//3, n//3)
            
    if x == n // 3 and y == n // 3:
                print(" ", end = " ")
    else:
        print("*", end = " ") 
                    

n = int(input())

paint(0, 0, n)

