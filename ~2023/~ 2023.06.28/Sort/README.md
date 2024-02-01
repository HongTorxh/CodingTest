## 18870

- 얕은 복사 : 얕은 복사는 변수를 복사했다고 생각했지만 실제로는 연결되있는 곳. 즉, 변수를 복사했지만 참조한 곳이 동일하기 때문에 같은 변수를 가르킴.
  - `=` 대입 연산자 : mutable한 객체인 리스트는 `=` 대입 연사자 이용시 얕은 복사가 됨. But, int형은 immutable한 객체이기 때문에 깊은 복사가 된다.
  - `[:]` 슬라이싱을 이용한 얕은 복사 : 리스트 내부 리스트에 접근시 얕은 복사가 됨.
  - `copy()`를 이용한 얕은 복사 : 위의 `[:]` 슬라이싱과 같음.
- 깊은 복사
  - 깊은 복사는 리스트 내부 리스트, 딕셔너리 내부 리스트 등 내부에 있는 개체 모두 새롭게 만들어주는 작업을 수행한다.
  - 깊은 복사를 사용하기 위해서는 copy 모듈의 deepcopy 함수를 사용해야 함.

```python
# 시간초과
import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

result = {}

for i in range(n):
    result[arr[i]] = 0

arr_2 = deepcopy(arr)

temp = set(arr)
temp = list(temp)
arr.sort()

length = len(temp)
for i in range(length):
    for j in range(i+1, length):
        if arr[i] == arr[j]:
            continue
        else:
            result[arr[j]] += 1

for i in arr_2:
    print(result[i], end=" ")

```

- 시간초과,, 딕셔너리 사용했는데 안된다.

```python
#시간 초과 버전 2
import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

temp = [deepcopy(arr), [0] * n]



temp[0].sort()

for i in range(1, n):
    if temp[0][i-1] == temp[0][i]:
        continue
    else:
       for j in range(i, n):
           temp[1][j] += 1

for i in range(n):
    for j in range(n):
        if temp[0][j] == arr[i]:
            print(temp[1][j], end = " ")
            break
```

- 2차원 배열을 사용해봤다. 더 느리다.

```python
# 성공 - 2시간 16분짜리 풀이
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
temp = {}

for i in range(len(arr2)):
    temp[arr2[i]] = i

for i in arr:
    print(temp[i], end=" ")
```

- 결국엔 sort, set, dictionary를 얼마나 잘 사용하냐의 문제였다. 나는 첫번째 풀이에서 너무 돌고돌아 2시간 넘게 걸렸다... 앞으로 방법을 좀더 제대로 생각해야겠다.
