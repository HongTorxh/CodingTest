import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lines = []
for _ in range(n):
    lines.append(int(input()))

# K가 10,000 이하의 정수, N이 1이상 1,000,000이기 때문에
# 순차 탐색 시 최대 10,000 * 1,000,000 = 10,000,000,000번 해야함
# 때문에 이분 탐색으로 진행

start = 1
end = max(lines)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for line in lines:
        # line < mid면 자를 수 없기 때문에 패스
        if line < mid:
            continue
        total += line // mid
    
    # total < k면 아직 부족하다는 것. 자르는 길이를 작게 해야함.
    if total < k:
        end = mid - 1
    # total >= k면 충분함. 하지만, 최대 랜선 길이를 구하기 위해선 끝까지 수행해봐야 함
    else:
        result = mid
        start = mid + 1

print(result)