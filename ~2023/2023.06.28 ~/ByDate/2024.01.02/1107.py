import sys
input = sys.stdin.readline

arr = [0] * 10

n = int(input())
m = int(input())
temp = list(map(int,input().split()))
for i in temp:
    arr[i] = 1

if n == 100:
    print(0)
else:
    n_arr = []
    k = n
    while True:
        if k < 10:
            n_arr.append(k % 10)
            break
        n_arr.append(k % 10)
        k = k // 10
    n_arr.reverse()
    for i in n_arr:
        j = 0
        while True:
            if arr[i+j] == 0 or arr[i-j]  
