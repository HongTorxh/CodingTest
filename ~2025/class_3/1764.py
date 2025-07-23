import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

dic = defaultdict(int)
for i in range(n+m):
    dic[input().strip()] += 1
result = []
for key, value in dic.items():
    if value == 2:
        result.append(key)

result.sort()
print(len(result))
for r in result:
    print(r)