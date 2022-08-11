# 검색(search)

- 저장되어있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목 찾기

## 검색의 종류

- 순차검색(sequential search)
- 이진검색(binary search)
- 해쉬(hash)

## 1. 순차 검색

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
- 가장 간단하고 직관적인 검색방법
- 배열이나 연결 리스트 등 순차 구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함

### 장점

- 단순하고 구현하기 쉽다

### 단점

- 검색 대상의 수가 많은 경우 수행시간이 급격히 증가

### 1.1 비정렬 자료 탐색

### 과정

1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
3. 자료 구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

### 특징

- 찾고자하는 원소의 순서에 따라 비교 회수 결정됨

### 시간 복잡도

- 1번째 원소 찾을 때 1번 비교 2번째 원소 찾을 때 2번 비교
- 정렬되지 않은 자료에서의 순차검색 평균 비교 횟수
    - = (1/n)*(1 + 2 + .. + n) = (n+1)/2
- 시간 복잡도 : O(n)

### 구현

```python
def sequentialsearch(a, n, key):
    i = 0
   
    while i<n and a[i] != key:
        i += 1
    
    if i < n:
        return i
    else:
        return -1
```

### 1.2 정렬 자료 탐색

### 과정

1. 오름차순이라고 가정
2. 순차적으로 검색하면서 키 값을 비교하여 원소의 키 값이 검색 대상 키 값보다 크면 찾는 원소가 없다는 것이므로 검색 중단

### 특징

- 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어든다.
- 

### 시간 복잡도

- 시간 복잡도 : O(n)

### 구현

```python
def sequentialsearch(a, n, key):
    i = 0
    while i < n and a[i] < key: # key보다 커지면 더이상 비교할 필요 없음
        i += 1

    if i < n and a[i] == key:
        return i
    else:
        return -1
```

---

## 2. 이진 검색(binary search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 정렬된 자료에 적용 가능

### 검색과정

1. 자료의 중앙에 있는 원소 고르기
2. 중앙 원소의 값과 찾고자 하는 목표 값 비교
3. 목표 값이 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행

### 구현

```python
def binarysearch(arr, N ,key):
    start = 0
    end = N-1

    while start <= end:
        middle = (start + end)//2
        if arr[middle] == key:
            return True

        elif arr[middle] > key:
            end = middle -1
        else:
            start = middle + 1

    return False
```

### 재귀함수를 사용한 구현

```python
def recursivebinarysearch(a, key, start, end):
    middle = (start + end )//2

    if start > end:
        return False
    elif key == arr[middle]:
        return True
    elif arr[middle] > key:
        end = middle - 1
    else:
        start = middle + 1

    recursivebinarysearch(a, key, start, end)

recursivebinarysearch(a, key, 0, n-1)
```