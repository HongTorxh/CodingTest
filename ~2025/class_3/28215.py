import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(list(map(int, input().split())))

combination = combinations(houses, k)
result = float('inf')
for combi in combination:
    temp = []
    for house in houses:
        if tuple(house) in combi:
            continue
        min_val = float('inf')
        for x, y in combi:
            distance = abs(house[0] - x) + abs(house[1] - y)
            if distance < min_val:
                min_val = distance
        temp.append(min_val)
    temp.sort()
    if temp[-1] < result:
        result = temp[-1]

print(result)
    