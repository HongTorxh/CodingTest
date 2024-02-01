## Dynamic Progamming

< 개념 >

- Dynamic Programming, 줄여서 DP는 하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용하는 것. 아고리즘이 아닌 하나의 문제해결 방법이라고 볼 수 있음. '재활용'이 중요한 키워드
- DP는 재귀랑 비슷한데 왜 사용할까? 일반적으로 재귀는 단순히 사용 시 동일한 작은 문제들이 여러 번 반복 되어 비효율적인 계산이 될 수 있기 때문이다. ex) 피보나치 수열의 경우 재귀로 해결 시 `f(n) = f(n-1) + f(n-2)` 으로 f(n-1), f(n-2)에서 각 함수를 1번씩 호출하면 동일한 값을 2번씩 구하게 된다. 때문에 이게 100번째 피보나치 수를 구하기 위해서는 호출되는 함수의 횟수가 기하급수적으로 증가한다.
- 이것을 DP로 해결하면 O(n^2) -> O(f(n))(다항식 수준으로, 문제에 따라 다름)로 개선
- DP의 사용 조건
  - Overlapping Subproblems
    - DP는 기본적으로 문제를 나누고 그 문제의 결과 값을 재활용하여 전체 답을 구한다. 따라서 동일한 작은 문제들이 반복하여 나타나는 경우 사용 가능.
  - Optimal Substructure
    - 부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우에 사용 가능하다.
- DP 사용법
  - 변수 파악하기
  - 변수 간 관계식 만들기 - 점화식
  - Memoization
  - 가장 작은 문제 파악하기
  - 구현
- 구현 방법
  - Bottom-up
    - 가장 아래에서부터 게산을 수행하고 누적시켜 전체 큰 문제를 해결하는 방식
    - dp[0]부터 반복문을 통해 점화식으로 dp[n]까지의 값을 전이시켜 재활용하는 방식
  - Top-down
    - dp[n] 값을 찾기 위해 위에서부터 바로 호출을 시작하여 dp[0]의 상태까지 내려가 구한다음 해당 결과 값을 재귀를 통해 전이시켜 재활용하는 방식.
    - 가장 최근의 상태 값을 메모해 두었다고 하여 Memoization