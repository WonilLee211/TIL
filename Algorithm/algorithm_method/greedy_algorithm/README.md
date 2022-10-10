
# 그리디 알고리즘

- 여러 경우 중 하나를 선택할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식
- 지역적 최적이지만 최종적인 최적의 답이라고 할 순 없다.
- 그리디 알고리즘으로 풀 수 있는지 확인해야 함

## -1. 동작과정

1. 해 선택
    - 현재의 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합에 추가
2. 실행 가능성 검사
    - 새로운 부분 해 집합이 실행가능한지 확인
    - 문제의 제약 조건을 위반하지 않는지 검사
3. 해 검사
    - 새로운 부분 해 집합이 문제의 해가 되는지 확인
    - 아직 전체 문제의 해가 완성되지 않았다면 1의 선택부터 다시 시작

## -2. 대표문제

- 최소 동전을 사용하는 거스름돈 구하기
- 배낭 짐싸기
    - 제한된 무게 내에서 물건의 값이 최대값이 되도록 담기

### 2.1 배낭 짐싸기

- 탐욕적 방법
    - 불가능
- 완전탐색방법
    - 무게 초과하는 집합 버리고 나머지 집합에서 총 값이 가장 큰 값 선택
    - 물건의 개수가 증가하면 시간복잡도 지수적으로 증가
- DP

### 2.2 활동 선택 문제

- 가능한 많은 회의가 열리기 위해 회의 배정
- **입력**
    - 회의 개수 10
    - (시작 시간, 종료 시간)
        - 1 4 1 6  6 10 5 7 3 8 5 9 3 5 8 11 2 13 12 14
- 시작시간과 종료시간이 있는 N개의 활동들이 집합에서 서로 겹치지 않는 최대 갯수의 활동들의 집합 구하기
- **탐욕기법 반복알고리즘**
    - 종료 시간 순으로 활동 정렬
    - 첫번째 활동 선택
    - 선택한 활동의 종료시간보다 빠른 시작시간을 가진 활동 제거
    - 남을 활동들에 대해 앞의 과정을 반복
    - 재귀 알고리즘
        
        ```python
        구현하기
        ```
        

### 2.3 탐욕 기법을 통한 baby-gin 문제 해결

- 완전 검색이 아닌 방법
- counts 배열 이용한 문제해결
- 반복
    
    ```python
    t = int(input())
    for tc in range(1, t + 1):
        card = int(input())
        c = [0] * 12
    
        i = 0
        while i < 6:
            c[card%10] += 1
            card //= 10
            i += 1
        tri = 0
        run = 0
    
        i += 1
        while i < 10:
            if c[i] >= 3:
                c[i] -= 3
                tri += 1
                continue
            if c[i] and c[i+1] and c[i+2]:
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
                run += 1
                continue
    
            i += 1
    
        if run + tri == 2:
            print(f'#{tc} baby gin}')
        else:
            print('lose')
    ```
    
### 2.4 큰 수 법칙 
```python

# 주어진 수를 m번 더해서 가장 큰 수를 만드는 법칙
# 같은 위치의 수를 k번 더할 수 없다.
# 논리1
# - 가장 큰 수를 k번 더하고 두번째 큰 수를 더한다. m 번이 채워질 때까지 반복

n, m, k = 5, 8, 3 
data = 2, 4, 5, 4, 6
m1 = m

data.sort()
first = data[-1]        # 가장 큰 수
second = data[-2]       # 두번째 가장 큰 수

result = 0


while True:
    for i in range(k):
        if m == 0:      # 연산 횟수가 끝나면 break
            break
        m -= 1
        result += first # k번 더하기
    
    if m == 0:          # 연산 끝나지 않았으면 second 더하기
        break
    result += second
    m -= 0
    
print(result)

# 논리2
# - 가장 큰 수가 더해지는 횟수와 두번째로 큰 수가 더해지는 횟수를 세기

cnt = 0                 # 가장 큰 수 더해지는 횟 수 계산
cnt += m1//(k + 1) * k + n % (k + 1)

result1 = cnt * first + (m1 - cnt) * second

print(result1)

```
<h6>(이것이 취업을 위한 코딩테스트다_그리디)</h6>

### 2.5 일이 될 때까지

```python
# n이 1이 될 때까지 아래 연산
# n이 k로 나눠떨어지는 수라면 나누기
# 아니라면 -1

n, k = 25, 3

cnt = 0
while True:
    t, v = divmod(n, k)

    if t == 0:
        if v > 1:
            cnt += v - 1
        break

    cnt += v + 1
    n = t

print(cnt)

```
<h6>(이것이 취업을 위한 코딩테스트다_그리디)</h6>

## -3. 탐욕 알고리즘의 **필수요소**

- 탐욕적 선택 속성 : 탐욕 선택이 항상 안정함을 증명해야 함
- 최적 부분 구조
    - 하나의 선택을 하면 풀어야 할 하난의 하위 문제가 남음
- `원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해`임을 증명해야 함

## - 4. 탐욕 기법과 동적 계획법의 비교

- 탐욕기법
    - 지역 최적해 선택
    - 하위 문제 풀기 전에 선택이 먼저 이루어짐
    - top-down방식
    - 일반적으로 빠르고 간결
- 동적계획법
    - 매 단계의 선택은 해결한 하위 문제의 해를 기반
    - 하위 문제가 우선 해결
    - bottom-up 방식
    - 좀 더 느리고 복잡
    