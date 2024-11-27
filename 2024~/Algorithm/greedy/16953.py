start, end = map(int,input().split())
cnt = 0

while end != start:
    if end == 0:
        cnt = -1
        break
    if end % 2 == 0:
        end = end // 2
        cnt += 1
    else:
        if end % 10 != 1:
            cnt = -1
            break
        end = end // 10
        cnt += 1
    
if cnt == -1:
    print(cnt)
else:
    print(cnt + 1)
