## 2. 이진 검색(binary search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 정렬된 자료에 적용 가능

### 검색과정
1. 자료의 중앙에 있는 원소를 고른다
2. 중앙 원소의 값과 찾고자하는 목표값 비교
3. 목표값이 중앙원소보다 값보다
    1.  작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행
    2. 크다면 자료의 오른쪽 반에 대해서  새로 검색 수행
4. 123 반복
   
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