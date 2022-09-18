# 조합
<h6>출처 : https://intrepidgeeks.com/tutorial/sorting-and-combining-using-python </h6>
- 조합의 경우 순서가 상관없기 때문에 순서가 역순인 경우는 출력하지 않아도 된다.
    - 즉 앞서 리스트에 추가한 숫자보다 큰 경우만 추가
    
## 구현1
- 재귀활용한 구현
```python
def comb(arr, n):
    result = []

    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)

    return result

arr = [1, 2, 3]
print(comb(arr, 1)) # [[1], [2], [3]]
print(comb(arr, 2)) # [[1, 2], [1, 3], [2, 3]]
print(comb(arr, 3)) # [[1, 2, 3]]
```


## 구현2
- itertools 모듈 사용
```python
import itertools

data = [1, 2, 3]

for i in itertools.combinations(data, 2):
    print(list(i), end=' ')
    
 # [1, 2] [1, 3] [2, 3] 
```