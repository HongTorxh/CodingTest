import sys
input = sys.stdin.readline

def isDemecal(n):
    global result
    flag = 0
    
    for j in range(2, n):
        if n % j == 0:
            flag = 0
            break
        flag = 1
    if n == 2:
        flag = 1
    if flag == 1:
        result += 1

n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in arr:
    isDemecal(i)

print(result)