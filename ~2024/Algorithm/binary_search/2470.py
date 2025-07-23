import sys
input = sys.stdin.readline

# 산성 용액 +
# 알칼리성 용액 -
# 두 용액 합쳐서 가장 0에 가까운 용액 찾기

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left, right = 0, n-1
result_sum = float('inf')
result = (0, 0)
while left < right:
    curr_sum = arr[left] + arr[right]

    if abs(curr_sum) < abs(result_sum):
        result_sum = curr_sum
        result = (arr[left], arr[right])
    
    if curr_sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])