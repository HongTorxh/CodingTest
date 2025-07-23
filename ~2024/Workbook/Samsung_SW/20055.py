import sys
from collections import deque
input = sys.stdin.readline

# 시뮬레이션 문제
# 벨트 회전을 하기 위서 배열에 저장하는데, appendleft를 위해 deque를 사용하는 것이 올바르다고 생각
# 조건에 부합하다면 마지막꺼를 빼고 appendleft를 한다.

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = [0] * n
# 내구도가 0인 칸의 개수
cnt = 0
# 현재 단계
level = 1

while True:
    # 1.한칸 회전
    tmp = belt.pop()
    belt.appendleft(tmp)
    robots = [False] + robots[:-1]
    robots[-1] = False
    # 2.가장 먼저 올라간 로봇부터 이동
    # 칸에 로봇이 있거나 내구도가 0이면 패스
    for i in range(n - 2, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i] = False
            robots[i + 1] = True
            belt[i+1] -= 1
    robots[-1] = False
    # 3. 0번 index의 내구도가 0이 아니면 로봇 올리기
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
    
    # 4. 내구도가 0인 칸의 개수가 K개인지 판단
    if belt.count(0) >= k:
        print(level)
        break
    # 과정이 끝났으니 level 추가
    level += 1
