# INDEX

- 반복과 재귀
- 완전검색기법
- 순열
- 부분집합
- 그리디 알고리즘
- 활동 선택 문제
- baby-jin

# 반복과 재귀

- 반복 : 수행하는 작업이 완료될 때까지 반복
- 재귀 : 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법

## -1. 반복구조

- **초기화**
    - 반복되는 명령문을 실행하기 전에 조건 검사에 사용할 변수의 초기값 설정
- 조건검사(check control expression)
- 반복할 명령문 실행(action)
- 업데이트(loop update)
    - 무한 루프(infinite loop)가 되지 않게 조건이 거짓이 되게 함

### 1.1 반복을 이용한 선택정렬

```python
def SelectionSort(A):
    n = len(a)
    
    for i in range(0, n-1):
        minI = i
        
        for j in range(i, n):
            if a[j] < a[minI]:
                minI = j
        a[minI], a[i] = a[i], a[minI]
```

### 1.2 재귀적 알고리즘

- 재귀적 정의
    1. 기본부분(basis part)
        - 집합에 포함되어 있는 원소로 induction을 생성하기 위한 시드역할
    2. 유도 부분(inductive case or rule)
        - 새로운 집합의 원소를 생성하기위해 결합되어지는 방법

### 1.3 재귀 함수

- 함수 내부에서 직접 간접적으로 자신을 호출하는 함수
- 구성
    1. 기본부분
    2. 유도부분
1. 함수 호출
    - 프로그램 메모리 구조에서 스택 사용
    - 성능 저하 발생
    

### 1.4 팩토리얼 재귀 함수

- 재귀적 정의
    - basis rule
        - N ≤ 1, n =1
    - inductive rule
        - N > 1, n! = n*(n-1)!
- n!에 대한 재귀함수
    
    ```python
    def fact(n):
        if n < 1: return 1 # basis part
        else: return n * fact(n-1) # inductive parte
    
    ```
    
- 반복과 재귀의 방법 선택
    1. 재귀는 설계가 간단하고 자연스러움
    2. 일반반복보다 메모리와 연산을 포함한다는 뜻
    
- 비교
    - 
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9d30595-ce5a-4a07-8fd7-00a9959d973e/Untitled.png)
    

### 연습문제

- 선택정렬을 재귀 알고리즘으로 작성
    
    ```python
     def SelectionsSort(s):
    if s == n-1:
        return

    MinI = s

    for j in range(s+1, n):
        if arr[MinI] > arr[j]:
            MinI = j
    arr[MinI], arr[s] = arr[s], arr[MinI]
    SelectionsSort(s+1)


    arr = [7, 1, 3, 5, 8, 6, 4, 2]
    n = len(arr)
    SelectionsSort(0)
    print(arr)
    ```
---
   

# Brute-Force

- force는 컴퓨터의 force를 의미
- brute-force 방법은 대부분 문제에 적용가능
- 상대적으로 빠른 시간에 문제해결 가능
- 문제에 포함됨 자료의 크기가 작다면 유용
- 학술적 또는 교육적 목적을 위해 알고리즘  효율성을 판단하기 위한 척도

## -1. 완전 검색

- 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 것
- 우선 완전탐색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직
- **순열과 조합, 부분집합 등의 조합적 문제들과 연관됨**
    - 완건점색은 조합적 문제에 대한 brute-force 방법



# 순열

- 서로 다른 것들 중 몇 개를 뽑아 한 줄로 나열하는 것
- nPr = n *( n -1 )* (n -  2)* …*(n - r + 1)
- 

## -1. 단순한 순열 생성 방법

```python
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 !+= i2:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3(
```

## -2. 최소 변경을 통한 방법

- 각각의 순열들은 이전 상태의 단지 2개의 요소들 교환을 통해 생성
- [**1**,2,**3**], [**3**,**2**,1], [2, **3**, **1**], [**2**, 1, **3**], [**3**, **1**, 2], [1, 3, 2]

## -3. 재귀호출을 통한 순열 생성

```python
# p[] : 데이터가 저장된 배열
# k : 원소의 개수, i : 선택된 원소의 인덱스
def perm(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[j], p[i] = p[i], p[j]
            perm(i + 1, k)
            p[j], p[i] = p[i], p[j]

p = [1, 2, 3]
perm(0, 3)
```

### 예제 swea 4881 최소합

```python
# p[] : 데이터가 저장된 배열
# k : 원소의 개수, i : 선택된 원소의 인덱스
def perm(i, k):
    global minV
    if i == k:      # 인덱스 i == 원소의 개수
        s = 0       # 모든 l행에서 p[l]열을 골랐을 때의 합
        for l in range(k):
            s += arr[l][p[l]]
        if minV > s:
            minV = s
        elif s >= minV:     # 백트래킹까지 구현할 수 있도록 하기
            return
    else:
        for j in range(i, k):
            p[j], p[i] = p[i], p[j]
            perm(i + 1, k)
            p[j], p[i] = p[i], p[j]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n) ]
    p = [i for i in range(n)]         # p[i] i행에서 선택한 열 번호
    minV = n * 10

    perm(0, n)
    print(f'#{tc} {minV}')
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/13de1aa7-5ab7-4436-8635-2d80ba16310a/Untitled.png)

## -4.사용 여부 배열을 이용한 순열

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87a1e6a3-88f4-46a0-bf1d-57d05c790a38/Untitled.png)

```python
# p[] : 순열을 저장하는 배열, arr[i] : 순열을 만드는데 사용할 숫자 배열
# n = 원소의 개수, i = 선택된 원소의 수
# used[N-1] : 사용 여부, p : 결과 저장 배열

def perm(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 사용됨으로 표시
                p[i] = a[j]     # p[j]는 a[j]로 결정
                perm(i+1, k)    # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 3
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * N
perm(0, N)
'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]'''
```

## -5. nPr

```python
# p[] : 순열을 저장하는 배열, arr[i] : 순열을 만드는데 사용할 숫자 배열
# n = 원소의 개수, i = 선택된 원소의 수
# used[N-1] : 사용 여부, p : 결과 저장 배열

def perm(i, r, k):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j] 사용됨으로 표시
                p[i] = a[j]         # p[j]는 a[j]로 결정
                perm(i+1, r, k)     # p[i+1] 값을 결정하러 이동
                used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 5
r = 3
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * r
perm(0, r, N)
```

### nPr : 특정 위치 값을 고정시켜 순열 구하기

```python
# p[] : 순열을 저장하는 배열, arr[i] : 순열을 만드는데 사용할 숫자 배열
# n = 원소의 개수, i = 선택된 원소의 수
# used[N-1] : 사용 여부, p : 결과 저장 배열

def perm(i, r, k):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j] 사용됨으로 표시
                p[i] = a[j]         # p[j]는 a[j]로 결정
                perm(i+1, r, k)     # p[i+1] 값을 결정하러 이동
                used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 5
r = 5
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * r
used[0] = 1
p[0] = 1
perm(1, r, N)
```

### 연습문제 : 완전검색을 통한 baby-gin 접근

- 고려할 수 있는 모든 경우의 수 생성하기
    - 6개로 만들 수 있는 모든 숫자 나열
- 해답 테스트
    - 앞의 3자리와 뒤의 3자리를 잘라, 테스트
6자리 숫자에 대해서 완전 검색을 적용하여 baby-gin을 검사하기

- 완전탐색을 통한 방법 : 재귀 조합
    
    ```python
    def f(i, k):
        if i == k:
            # print(card)
            run = 0
            triplet = 0
            if card[0] == card[1] and card[1] == card[2]:
                triplet += 1
            if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
                run += 1
            if card[3] == card[4] and card[4] == card[5]:
                triplet += 1
            if card[3] + 1 == card[4] and card[4] + 1 == card[5]:
                run += 1
            if triplet + run ==2:
                return 1
            else:
                return 0
            
        else:
            for j in range(i, k):
                card[i], card[j] = card[j],card[i]
                if f(i+1, k):
                    return 1
                card[i], card[j] = card[j], card[i]
            return 0
        
    t = int(input())
    for tc in range(1, t + 1):
        card = list(map(int, input()))
        ans = f(0, 6)
        if ans:
            print(f'#{tc} baby gin')
        else:
            print(f'#{tc} lose')
    ```

---

# 부분집합

- 집합에 포함된 원소들을 선택
- 최적의 부분집합 찾기 중요
- N개의 원소를 포함한 집합
    - power set : 2**n개
    - 원소 수가 증가하면 부분집합의 개수는 지수적으로 증가

## -1. 바이너리 카운팅(binary counting)

- 원소 수에 해당하는 N개의 비트열 이용
- n번째 비트 값이 1이면 n번째 원소가 포함되었음을 의미

```python
arr= [3, 6, 7, 1, 5, 4]
n = len(arr)
temp = []
for i in range((1<<n)):         # 1<<n : 부분집합의 개수
    for j in range(0, n):       # 원소의 수만큼 비트를 비교함
        if i & (1<<j):          # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=' ')
    print()
```

```python
#재귀
def f(i, k):
    if i == k:
        # print(bit)
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        f(i+1,k)
        bit[i] = 1
        f(i+1,k)

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
bit = [0] * n
f(0, n)
```

# 조합

- 서로 다른 n개의 원소 중에서 r개를 순서없이 골라낸 것
- `nCr = n!/( (n-r)!*r! ), (n≥r)`
- 재귀적 표현 : nCr = (n-1)C(r-1) + (n-1)Cr
    - 마지막 한 개가 포함된 경우 + 마지막 한 개가 포함되지 않은 경우
    - 
        
        ```python
        def nCr(n, r, s):
            if r == 0:
                print(*comb)
            else:
                for i in range(s, n-r+1):
                    comb[r-1] = A[i]
                    nCr(n, r-1, i+1)
        
        A = [1, 2, 3, 4, 5]
        n = len(A)
        r = 3
        
        comb = [0] * r
        nCr(n, r, 0)
        '''
        3 2 1
        4 2 1
        5 2 1
        4 3 1
        5 3 1
        5 4 1
        4 3 2
        5 3 2
        5 4 2
        5 4 3'''
        ```
        
    
    ### 연습문제
    
    - 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 부분 집합 모두 출력
        
        ```python
        arr = [-1, 3, -9, 6, 7,-6, 1, 5, 4, -2]
        
        ```
        

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

## -5. 대표적 탐욕 기법의 알고리즘

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/231a86bc-f93f-4689-b5b8-213dd2b0513e/Untitled.png)