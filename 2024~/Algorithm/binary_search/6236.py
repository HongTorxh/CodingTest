import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bankbook = []
for _ in range(n):
    bankbook.append(int(input()))

# M번을 맞추어 인출할 때,
# K원 인출해 사용하는 경우 필요한 최소 금액 K를 계산
# 모든 날에 돈을 이용해야 하기 때문에
# 최소는 max값, 최대는 다 더한 값일 것이다.

start = max(bankbook)
end = sum(bankbook)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    curr = 0 # 현재 합
    for money in bankbook:
        if curr + money > mid:
            cnt += 1
            curr = money
        else:
            curr += money
    
    # 만약 cnt <= m 이면 금액을 더 낮추어도 된다는 것
    if cnt <= m:
        result = mid
        end = mid - 1
    # cnt > m 이면 현재 값이 너무 낮아서 안된다는 뜻
    else:
        start = mid + 1

print(result)