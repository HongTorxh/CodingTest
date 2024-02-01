import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)

arr.sort()

temp = arr[n-1] - arr[0] - 17
left = []
right = []
for i in range(temp+1):
    left.append(arr[0] + i)
    right.append(arr[n-1] - (temp - i))

result = 1000000
for i in range(len(left)):
    minimum = 0
    for j in range(n):
        if(arr[j] < left[i]): 
            minimum += (left[i] - arr[j]) ** 2
        if(arr[j] > right[i]):
            minimum += (arr[j] - right[i]) ** 2
    if(minimum < result):
        result = minimum

print(result)