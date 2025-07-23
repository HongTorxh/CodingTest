import sys, copy
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
result = [0] * (n)
dic = defaultdict(int)

# 복사 후 정렬
nums_copy = copy.deepcopy(nums)
nums_copy.sort()

# 정렬한 값으로 순위를 매김
i = 0
for num in nums_copy:
    if num in dic.keys():
        continue
    dic[num] += i
    i += 1

for num in nums:
    print(dic[num], end = " ")