import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
dic = defaultdict(int)
country = defaultdict(list)
for _ in range(n):
    inp = list(map(int, input().split()))
    tmp = tuple(inp[1:])
    dic[tmp] += 1
    country[inp[0]] = tuple(inp[1:])

sorted_dic = dict(sorted(dic.items(), key = lambda x : x[0], reverse=True))

c = country[k]
result = 0
for idx, value in enumerate(sorted_dic.items()):
    if c == value[0]:
        print(result + 1)
    else:
        result += value[1]