# DP(Dynamic Programming) 동적계획 알고리즘
좀 더 조사-공부하기
- 최적화 문제를 해결하는 알고리즘
- ex> 그리디 알고리즘
- 같은 인풋에 대한 반복되는 호출을 하는 솔루션을 만났을 때, 즉 중복 컴퓨팅을 개선하는 방법론
- 입력 크기가 작은 부분들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 문제 해결하는 순

## 종류

1. memoization 
    - 함수의 중복호출을 방지하고자 결과를 저장하는 것
    - top down
2. tabulation
    - 도표를 작성이라는 뜻
    - 입력 크기가 작은 부분부터 해결하면서 그 해들을 이용하여 보다 큰 크기의 문제 해결
    - bottom up
    
## memoization
- 컴퓨터 프로그램을 실행할 때 **이전에 계산한 값을 메모리에 저장**하여 매번 다시 계산하지 않도록 전체적인 실행 속도를 빠르게 하는 기술
- 동적 계획법의 핵심이 되는 기술
- 메모리에 넣기라는 의미
- ~~memorization 아님 주의~~
- fibo(n)을 계산하자마자 저장하면(memoize) 실행 시간을 O(n)으로 줄일 수 있다.

### 구현1
```python
def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1[n-1] + fibo1[n-2])
    
    return memo[n]

memo = [0, 1]
print(fibo1(10)) # 55
```
### 구현2
```python
def fibo2(n):
    if memo[n]==-1:
        memo[n] = fibo2(n-1) + fibo2(n-2)
    return memo[n]

memo = [-1] * 101
memo[0] = 0
memo[1] = 1

for i in range(101):
    print(i, fibo2(i))

```

## tabulation
1. 문제를 부분 문제로 분할
2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다.
3. 그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.

```python
def fibo3(n): # iterative 방식 : fib2()
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[n-1] + f[n-2])

    return f[n]
```

- 정리하자면, DP는 재귀함수를 interative 방식으로 수행해서 부분 문제를 저장하고 각 문제를 해결해서 종합하는 방식
- 반복적 구조로 DP를 구현하는것이 효율적
