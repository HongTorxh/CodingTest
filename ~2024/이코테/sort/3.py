n = int(input())
arr = []

for _ in range(n):
    tmp = list(map(str, input().rstrip().split(" ")))
    arr.append((tmp[0], int(tmp[1])))

arr.sort(key = lambda x : x[1])

print(" ".join(i[0] for i in arr))
