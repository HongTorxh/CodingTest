import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 나무의 최대 갯수가 1,000,000, 최대 높이가 2,000,000,000 이기 때문에
# 순차적으로 탐색하면 시간 초과 발생 가능성이 있음
# 이분 탐색으로 진행

start = 0
end = max(trees)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for tree in trees:
        # 낮은 나무는 잘리지 않기 때문에 넘기기
        if tree < mid:
            continue
        total += tree - mid

    # total이 m보다 작다는 것은 아직 가져갈게 더 필요하다는 뜻. 즉, 더 낮은 높이에서 잘라야 한다.
    if total < m:
        end = mid - 1
    # total이 m보다 크거나 같다는 것은 높이가 충분하다는 것. 하지만, 적어도 m미터이므로 끝까지 탐색해야 하기 때문에 높이를 높여가며 탐색해줌
    else:
        result = mid
        start = mid + 1

print(result)