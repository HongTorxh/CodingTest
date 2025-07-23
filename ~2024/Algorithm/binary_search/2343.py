import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

# lessons를 m개의 블루레이로 분리할 때, 모든 블루레이를 만족하는 크기의 최솟값 찾기
# 이분 탐색으로 진행
# 무조건 하나의 강의를 포함하여야 하기에 max(lessons)가 최소 크기
# 최대 크기는 sum(lessons)

start = max(lessons)
end = sum(lessons)
reuslt = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    curr = 0 # 현재 녹화된 강의의 합
    for lesson in lessons:
        if curr + lesson > mid:
            cnt += 1
            curr = lesson
        else:
            curr += lesson
    # 블루레이 개수가 M 이하면 줄여도 된다는 것
    if cnt <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1



print(result)