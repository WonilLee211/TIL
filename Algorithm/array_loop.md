# 2차원 배열의 접근

## 1. 배열순회

- n X m 배열의 모든 원소 조사하는 방법

## 2. 지그재그 순회

```python
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1 -2*j)*(i%2)]
```

## 3. <mark>델타를 이용한 2차 배열 탐색</mark>

- 2차원 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방버

```python
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

for i in range(1, n-1):
    for j in range(1, n-1):
        for k in range(4):
            if 0 <= i + dx[k] < n and 0 <= i + dy[k] < n:
                arr[i + dy[k]][i + dx[k]]
```

## 4. 전치행렬

- 대각 대칭

```python
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

- zip 사용

```python
b = list(zip(*arr))
```

## 연습문제 1

- 5x5 2차 배열에 무직위로 25개의 숫자로 초기화 한 후 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값 구하기

```python
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

total = 0
for i in range(5):
    for j in range(5):
        for k in range(4):
            if 0 < i + dx[k] < n and 0 < j + dy[k] < n:
                total += abs(arr[i+dy[k]][j+dx[k]] - arr[i][j])
```

## 연습문제2_부분집합 합

- 유한 개의 정수로 이루어진 집합이 있을 때 이 집합의 부분 집합 중에 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지 알아내는 프로그램

```python
def subset(numbers):

    for i in range(1, 1<<10):
        subtotal = 0
        for j in range(10):
            if i & (1<<j):
                subtotal += numbers[j]
        if subtotal == 0:
            return 1
    return 0

if __name__ == '__main__':
    T = int(input())
    for test_case in range(1, T+1):
        numbers = list(map(int, input().split()))

        print(f"#{test_case}
```