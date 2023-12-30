import sys
input = sys.stdin.readline

t = int(input())

for i in range(0,t):
    n = int(input())
    result = 0
    if n < 5:
        print(0)
        continue
    temp = 5
    while(1): 
        if temp > n:
            break
        result += n // temp
        temp *= 5
    print(result)