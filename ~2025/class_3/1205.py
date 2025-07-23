import sys

input = sys.stdin.readline

n, taesoo, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
else:
    print(1)
    sys.exit()

scores.sort(reverse=True)
rank = 1
for score in scores:
    if taesoo < score:
        rank += 1
    elif taesoo == score:
        continue
    else:
        break

if n < p or taesoo > scores[-1]:
    print(rank)
else:
    print(-1)
