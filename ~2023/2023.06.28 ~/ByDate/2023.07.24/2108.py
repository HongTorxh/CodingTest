import sys, math
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr) / n))
print(arr[n//2])

dict = {}

for i in range(n):
    if arr[i] in dict:
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1

result = [k for k,v in dict.items() if max(dict.values()) == v]

if(len(result) >= 2):
    print(result[1])
else:
    print(result[0])

print(arr[n-1] - arr[0])
