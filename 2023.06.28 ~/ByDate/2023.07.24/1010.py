import sys
input = sys.stdin.readline

def fac(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp

n = int(input())

for i in range(n):
    n, m = map(int, input().split())
    result = fac(m) // (fac(m-n) * fac(n))
    print(result)