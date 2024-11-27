n = int(input())
arr = []
for i in range(n):
    a, b = map(int,input().split())
    arr.append([a,b])

arr.sort(key = lambda x: (x[1], x[0]))

print(arr)
count = 0
end_value = 0
for start, end in arr:
    if start >= end_value:
        count += 1
        end_value = end

print(count)