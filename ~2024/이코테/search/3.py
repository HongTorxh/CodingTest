# 떡볶이 떡 만들기
# 떡볶이 떡 길이가 일정하지 않음, 떡의 총길이는 맞춰준
# 높이를 지정하면 줄지어진 떡을 한번에 절단
# ex) 19, 14 10 17 / H = 15면, 15, 14, 10, 17이 될 것임. 
# 적어도 M만큼의 떡을 가지기 위한 높이의 최댓값 구하기
# [입력 조건]
# 첫 줄 : 떡의 개수 N, 요청 길이 M
# 둘째 줄 : 떡의 개별 높이

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

# n의 최댓값이 1,000,000만이기 때문에 1부터 차례대로 높이를 높여가는건
# 최악의 경우, 2,000,000,000 * 1,000,000을 해야하므로 불가능
# 따라서, m의 최솟값이 1이므로 최솟값 <= h <= 최댓값을 기준으로 구하면 될듯

start = min(rice_cakes)
end = max(rice_cakes)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for rice_cake in rice_cakes:
        if rice_cake < mid:
            continue
        total += rice_cake - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)

