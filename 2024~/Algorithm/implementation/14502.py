from itertools import combinations
from collections import deque
import copy

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스를 퍼뜨리는 함수
def spread_virus(lab, N, M):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx, ny))

# 안전 영역 크기를 계산하는 함수
def get_safe_area(lab, N, M):
    safe_count = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                safe_count += 1
    return safe_count

# 메인 함수
def solution(N, M, lab):
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
    max_safe_area = 0

    # 빈 칸 중 3개의 위치를 선택해 벽을 세우는 모든 경우의 수 확인
    for walls in combinations(empty_spaces, 3):
        # 실험을 위한 임시 연구소 복사
        temp_lab = copy.deepcopy(lab)

        # 선택된 위치에 벽 세우기
        for x, y in walls:
            temp_lab[x][y] = 1

        # 바이러스를 퍼뜨리기
        spread_virus(temp_lab, N, M)

        # 안전 영역의 크기 계산
        safe_area = get_safe_area(temp_lab, N, M)
        max_safe_area = max(max_safe_area, safe_area)

    return max_safe_area

# 입력 받기
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(solution(N, M, lab))
