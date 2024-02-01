import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
flag = 0
for i in range(n):
    temp = int(input())
    if temp == k:
        flag = 1
        print(1)
    elif temp > k:
        continue
    elif temp < k:
        arr.append(temp)

length = len(arr)

cnt = 0
while k > 0:
    for i in range(len(arr)-1, -1, -1):
        if (k - arr[i]) >= 0:
            cnt = k // arr[i]
            k =  k % arr[i]
            break

if flag == 0:
    print(cnt)