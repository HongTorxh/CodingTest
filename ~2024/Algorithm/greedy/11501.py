import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    sub = []
    max_value = -1
    result = 0
    for j in range(n-1, -1 , -1):
        if arr[j] > max_value:
            for num in sub:
                result += max_value - num
            max_value = arr[j]
            sub.clear()
        else:
            sub.append(arr[j])
    for num in sub:
        result += max_value - num
    print(result)