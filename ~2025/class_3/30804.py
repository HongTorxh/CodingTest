# 2025.07.23 2
# 과일 탕후루
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
fruit = list(map(int, input().split()))
dic = defaultdict(int)
left = 0
max_len = 0
for right in range(n):
    dic[fruit[right]] += 1
    while len(dic) > 2:
        dic[fruit[left]] -= 1
        if dic[fruit[left]] == 0:
            del dic[fruit[left]]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)
