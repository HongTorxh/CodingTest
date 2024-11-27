import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

# r연산인지 c연산인지
flag = False
time = 0
while True:
    if r-1 < len(arr) and c-1 < len(arr[0]):
        if arr[r-1][c-1] == k:
            print(time)
            break
    if time > 100:
        print(-1)
        break

    if len(arr) >= len(arr[0]):
        flag = False
    else:
        flag = True
    if not flag:
        new_arr = []
        for i in range(len(arr)):
            dic = {}
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    continue
                if arr[i][j] in dic.keys():
                    dic[arr[i][j]] += 1
                else:
                    dic[arr[i][j]] = 1
            sorted_arr = sorted(dic.items(), key = lambda x : (x[1], x[0]))
            new_col = []
            for num, cnt in sorted_arr:
                new_col.extend([num,cnt])
            new_arr.append(new_col)
        max_length = max(len(col) for col in new_arr)
        for col in new_arr:
            col.extend([0] * (max_length - len(col)))
        
    else:
        new_arr = []
        transpose = list(zip(*arr))
        for i in range(len(transpose)):
            dic = {}
            for j in range(len(transpose[i])):
                if transpose[i][j] == 0:  # 0은 무시
                    continue
                if transpose[i][j] in dic:
                    dic[transpose[i][j]] += 1
                else:
                    dic[transpose[i][j]] = 1
                
            sorted_arr = sorted(dic.items(), key = lambda x : (x[1], x[0]))
            new_col = []
            for num, cnt in sorted_arr:
                new_col.extend([num,cnt])
            new_arr.append(new_col)
        max_length = max(len(col) for col in new_arr)
        for col in new_arr:
            col.extend([0] * (max_length - len(col)))
        new_arr = list(zip(*new_arr))
    # arr를 new_arr로 변경
    arr = new_arr
    
    time += 1

