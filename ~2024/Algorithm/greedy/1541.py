arr = input().split('-')
result = []
for i in arr:
    s = 0
    tmp = i.split('+')
    for j in tmp:
        s += int(j)
    result.append(s)

answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]

print(answer)