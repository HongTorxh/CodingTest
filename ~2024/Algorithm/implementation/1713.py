import sys
from collections import deque
input = sys.stdin.readline

# 우선 0으로 초기화
# 추천시 +
# 안 비어있으면 추천 수가 가장 낮은거 delete
# 중복일 경우 오래된 순으로 delete
# 삭제되는 경우 0으로 수정
n = int(input())
t = int(input())
recommends = list(map(int, input().split()))

# 기록 되면 index를 기록
idx = 1
# (번호, 추천 수 , idx)
frames = []
for recommend in recommends:
    flag = False
    for i in range(len(frames)):
        if recommend == frames[i][0]:
            frames[i][1] += 1
            flag = True
    if not flag:
        if len(frames) == n:
            min_value = float('inf')
            min_frames = []
            for i in range(len(frames)):
                if min_value > frames[i][1]:
                    min_frames = []
                    min_frames.append((i, frames[i][2]))
                    min_value = frames[i][1]
                elif min_value == frames[i][1]:
                    min_frames.append((i, frames[i][2]))
            if len(min_frames) == 1:
                del frames[min_frames[0][0]]
            else:
                min_frames.sort(key = lambda x : x[1])
                del frames[min_frames[0][0]]
        frames.append([recommend, 1, idx])
        idx += 1

frames.sort(key = lambda x : x[0])

print(" ".join(str(frames[i][0]) for i in range(len(frames))))
