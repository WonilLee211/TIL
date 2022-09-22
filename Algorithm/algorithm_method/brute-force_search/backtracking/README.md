# BackTraking
## 1. 백트래킹이란?
- 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾는 기법
- 완전탐색 알고리즘이나, 상태공간을 트리로 나타낼 수 있을 때 적합한 방식
- 일종의 트리 탐색 알고리즘
- BFS, DFS, 최선 우선 탐색에 적용 가능

## 2. 백트래킹 구현에서 중요한 2가지
1. promising function
    - 유망한 답을 얻기 위해 세우는 함수로, state space tree의 모든 경우의 수를 볼 수 없으므로 유망한 답만 추려내는 함수
    - 이를 통해 가지치기 수행
2. 가지치기
## 3. 적용 문제
1. 최적화 문제
2. 결정 문제
   - 문제의 조건을 만족하는 해가 존재하는지 여부를 yes or no가 답하는 문제
     - 미로 찾기 : 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제
     - n-Queen 문제
     - Map-coloring
     - 부분 집합의 합(subset sum)문제 등

## 4. DFS와 백트래킹
### DFS
- 가능한 모든 경로를 탐색
- 불필요할 것 같은 경로를 사전에 차단하는 등의 행동이 없s으므로 경우의 수를 줄이지 못함
- 그래서 N!가지의 경우의 수를 가진 문제는 DFS로 처리 불가능
### 백트래킹
- 해를 찾아가는 도중 지금의 경로가 해가될 것 같지 않으면 그경로를 더 이상 가지 않고 되돌아 감.
- 즉, 코딩에서는 반복문의 횟수까지 줄일 수 있으므로 효율적
- 이를 **가지치기**라고 하는데, 불필요한 부분은 쳐내고 최대한 올바른 쪽으로 간다는 의미
> 결론 : 모든 가능한 경우의 수에서 특정한 조건을 만족하는 경우만 살펴보는 것
> 주로 완전 탐색 과정에서 조건문 등을 걸어 답이 절대 될 수 없는 상황을 정의하고 그러한 상황일 경우에는 탐색을 중지시킨 뒤 다른 경우를 탐색하도록 구현

## 5. 백트래킹 기법의 유망성 판단
- 어떤 노드의 유망성, 즉 해가 될 만한지 판단한 후 유망하지 않다고 결정되면 그 노드의 이전(부모)로 돌아가(backtracking) 다음 자식 노드로 갑니다.
- 해가 될 가능성이 있으면 유망하다(promising)고 하며, 유망하지 않는 노드에 가지 않는 것을 가지치기(pruning)한다고 하는 것

## 6. DFS에서 백트래킹 구현
- Baekjoon_9663번 N-Queen 문제가 대표적
    - 문제 : N*N크기의 체스판에 N개의 퀸이 서로 공격할 수 없게 놓는 경우의 수 구하기
    - promising function의 선별 조건 3가지
        1. 같은 행에 존재하면 안됨
        2. 같은 열에 존재하면 안됨
        3. 같은 대각에 존재하면 안됨

```python

def is_promising(r):
    # 열과 대각선상에 있는지 확인하기
    for i in range(r):
        if chessfield[r]  == chessfield[i] or abs(chessfield[r] - chessfield[i]) == abs(r - i):
            return False

    return True

def dfs(r):

    global cnt
    
    if r == n:
        cnt += 1
        return
    
    for i in range(n):
        chessfield[r] = i
        # 현재의 위치가 유망하다면
        if is_promising(r):
            # 다음 열에서 유망한 위치 찾기
            dfs(r+1)
        
n = int(input())
cnt = 0
chessfield = [0 for _ in range(n)]
dfs(0)
print(cnt)

```
---

## 7. 백트래킹 연습
### 백트래킹으로 부분집합 구하기
- n개의 원소가 들어있는 집합의 n**2개의 부분 집합을 만들 때는, True, False값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
```python
def backtrack(a, cnt, depth):
    c = [1, 0]

    if cnt == depth:
        print(a)# 답이면 원하는 작업을 한다
        return
    else:
        cnt += 1

        for i in range(2):
            a[cnt] = c[i]
            backtrack(a, cnt, depth)

nmax = 4
a = [0] * nmax
backtrack(a, 0, 3)
```
```python
numbers = list(range(1, 6))
selected = [False]*len(numbers)
result = []

def powerset(idx):
    if idx > len(numbers):
        selected[idx] = True
        powerset(idx + 1)
        selected[idx] = False
        powerset(idx + 1)
    else:
        res = []
        for i in range(len(numbers)):
            if selected[i]:
                res.append(numbers[i])
        result.append(res)
```
- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합
```python
def dfs(n, i):
    global answer
    global cnt # 재귀 횟수 세기
    cnt += 1
    if i == n:
        subsum = 0
        for i in range(n):
            if bit[i]:
                # print(arr[i], end = ' ')
                subsum += arr[i]
        # print()
        if subsum == 30:
            answer += 1
    else:
        bit[i] = 1
        dfs(n, i + 1)
        bit[i] = 0
        dfs(n, i + 1)
        
arr = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
n = len(arr)
bit = [0] * n
cnt = answer = 0
dfs(n, 0)
print(answer, cnt) # 39 2047
```
- 백트래킹 : 목표값보다 큰 경우
```python

def dfs(n, i, subsum):
    global answer
    global cnt
    cnt += 1
    if subsum > goals:
        return
    
    if i == n:
        if subsum == goals:
            answer += 1
        return

    else:
        dfs(n, i+1, subsum + arr[i])
        dfs(n, i+1, subsum)
            
arr = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
n = len(arr)
goals = 30
cnt = answer = 0
dfs(n, 0, 0)
print(answer, cnt) # 39 1843
```
- 백트래킹 : 남은 값을 더해도 목표값보다 작은 경우
```python
def dfs(n, i, subsum):
    global answer
    global cnt
    cnt += 1
    
    if subsum > goals:
        return
    if goals > subsum + tabul[i]:
        return
    if i == n:
        if subsum == goals:
            answer += 1
    else:
        dfs(n, i + 1, subsum + arr[i])
        dfs(n, i + 1, subsum)

arr = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
n = len(arr)

tabul = [0] * (n+1)
tabul[-1] = arr[-1]
for i in range(n-1, -1 , -1):
    tabul[i] += arr[i] + tabul[i + 1]
    
goals = 30
cnt = answer = 0
dfs(n, 0, 0)
print(answer, cnt) # 39 1775

```

### 백트래킹으로 순열구하기

```python
arr = [1, 2, 3]
n = len(arr)
r = 2 # 원하는 수열의 길이

def dfs(n, r, i):
    if i == r:
        print(arr[:r])
    else:
        for j in range(n):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(i+1, n, r);
            arr[i], arr[j] = arr[j], arr[i]

dfs(n, r, 0)
```
- 참고
```python
def backtrack(a, cnt, depth):
    global maxcondidates
    c = [0] * maxcandidates

    if cnt == depth:
        for i in range(1, cnt + 1):
            print(a[i], end=' ')
        print()
    else:
        cnt += 1
        ncandidates = construct_candidates(a, cnt, depth, c)
        for i in range(ncandidates):
            a[cnt] = c[i]
            backtrack(a, cnt, depth)

def construct_candidates(a, cnt, depth, c):
    in_perm = [False] * nmax
    for i in range(1, cnt):
        in_perm[a[i]] = True

    ncandidates = 0

    for i in range(1, depth + 1):
        if in_perm[i] == i:
            c[ncandidates] += 1
    return ncandidates
```

