import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

result = abs(100 - n)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):

        if int(nums[j]) in arr:
            break

        elif j == len(nums) - 1:
            result = min(result, abs(int(nums) - n) + len(nums))
