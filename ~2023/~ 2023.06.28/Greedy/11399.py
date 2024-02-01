import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

arr.sort()

result = 0

for i in range(0, n):
    result += arr[i] * (len(arr) - i)
    
print(result)