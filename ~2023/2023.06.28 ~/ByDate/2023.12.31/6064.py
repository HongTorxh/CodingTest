import sys
input = sys.stdin.readline



def findK(M, N, x, y):
    k = x
    while k <= M * N:
        if (k-x) % M == 0 and (k-y) % N == 0:
            return k 
        k += M
    return -1 

t = int(input())

for i in range(0, t):
    M,N,x,y = map(int,input().split())
    print(findK(M, N, x, y))


    
        
    
