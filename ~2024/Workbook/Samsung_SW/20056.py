import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[0] * n for _ in range(n)]

# 북 북동 동 동남 남 남서 서 북서
move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

fireballs = []
for _ in range(m):

    fireballs.append(list(map(int, input().split())))

cnt = 0
while True:
    
    if cnt == k:
        break
    # 1. 모든 파이어볼이 방향 속력으로 이동
    dic = {}
    curr_fireballs = []
    for fireball in fireballs:
        # 0 : r, 1 : c, 2: 질량, 3: 속력, 4: 방향
        r, c, m, s, d = fireball[0] - 1, fireball[1] - 1, fireball[2], fireball[3], fireball[4]
        
        # d 방향으로 s만큼 이동
        nr = r + (s * move[d][0])
        nc = c + (s * move[d][1])
        if nr < 0:
            nr = n + nr
        elif nr >= n:
            nr = nr % n
        if nc < 0:
            nc = n + nc
        elif nc >= n:
            nc = nc % n
        if (nr, nc) in dic.keys():
            dic[(nr,nc)] += 1
        else:
            dic[(nr,nc)] = 1

        curr_fireballs.append([nr, nc, m, s, d])
    
    print("curr------")
    for fireball in curr_fireballs:
        print(fireball)
    print("-------")
    # 2.이동을 모두 마침
    # 2개 이상의 파이어볼이 있는지 확인하기
    dup = []
    for key, value in dic.items():
        if value > 1:
           dup.append(key)
    if len(dup) == 0:
        fireballs = curr_fireballs
        cnt += 1
        continue
    # 파이어볼 합치기
    new_fireballs = []
    curr = set()
    while dup:
        nr, nc = dup.pop()
        weight = 0 # 질량 합
        odd, even = 0, 0
        speed = 0 # 속력 합
        tmp = 0
        
        for fireball in curr_fireballs:
            r, c, m, s, d = fireball[0], fireball[1], fireball[2], fireball[3], fireball[4]
            
            if r == nr and c == nc:
                weight += m
                speed += s
                tmp += 1
                if d % 2 == 0: # 짝수인 경우
                    even += 1
                else: 
                    odd += 1
            else:
                curr.add((r,c,m,s,d))
        weight = weight // 5
        speed = speed // tmp

        if weight == 0:
            continue

        if odd == 0 or even == 0:
            for i in [0,2,4,6]:
                new_fireballs.append([nr, nc, weight, speed, i])
        else:
            for i in [1,3,5,7]:
                new_fireballs.append([nr, nc, weight, speed, i])
    
    fireballs = new_fireballs
    for i in curr:
        fireballs.append([i[0],i[1],i[2],i[3],i[4]])
    cnt += 1
    print("new------")
    for fireball in fireballs:
        print(fireball)
    print("-------")
result = 0
for fireball in fireballs:
    result += fireball[2]

print(result)
