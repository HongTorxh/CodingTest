import sys
from collections import defaultdict
input = sys.stdin.readline

# 1. 팀당 6명의 주자가 되는지 확인하기
# 2. 확인 후 점수 계산하기

t = int(input())
for _ in range(t):
    n = int(input())
    players = list(map(int, input().split()))
    team_count = defaultdict(int)
    for player in players:
        team_count[player] += 1
    rank = 1
    team_rank = [[] * 6 for _ in range(len(team_count) + 1)] 
    for player in players:
        if team_count[player] < 6:
            continue
        team_rank[player].append(rank)
        rank += 1
    min_val = float('inf')
    result = -1
    for idx, t in enumerate(team_rank):
        if sum(t) != 0 and sum(t[:4]) < min_val:
            min_val = sum(t[:4])
            result = idx
        elif sum(t[:4]) == min_val:
            if t[-2] < team_rank[result][-2]:
                result = idx
    print(result)