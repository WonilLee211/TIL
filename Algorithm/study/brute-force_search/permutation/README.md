# 순열(pernutation)
<h6>참조 : https://m.blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=ssang8417&logNo=222147007019</h6>
<h6>참조 : https://bcp0109.tistory.com/14</h6>
## 1. 순열이란?
- 서로 다른 n개 중 r개를 골라 순서를 고려하여 나열한 경우의 수
- 순서가 부여된 임의의 집합을 다른 순서로 뒤섞는 연산
- nPr : n!/(n-r)!

![Alt text](../../../img/permutation.png)
## 2. 순열 구하는 방법
### 2.1 재귀함수와 swap함수를 이용해 배열 값을 직접 변경하여 순열을 구하는 방법
1. swap함수 만들어서 배열들을 직접 바꾸기
2. 배열의 첫 값부터 순서대로 하나씩 바꾸며 모든 값을 한번씩 swap
3. depth 기준 인덱스로 depth보다 인덱스가 작은 값들은 그대로 고정하고 depth보다 큰 값들만 가지고 다시 swap
- 간단하고 코드도 깔끔하게 나오지만 순열의 순서가 보장되지 않음

```python
def permutation(arr, depth, n, r):
    if depth == r:
        print(arr[:r])
        return

    for i in range(depth, n):
        swap(arr, depth, i)
        permutation(arr, depth + 1, n, r)
        swap(arr, depth, i)

def swap(arr, depth, i):
    arr[i], arr[depth] = arr[depth], arr[i]


arr = [1, 2, 3]
permutation(arr, 0, 3, 2)
```

### 2.2 재귀함수와 visited 배열을 이용하여 처리한 위치에 대해 참으로 설정하여 순열을 구하는 방법(DFS-backtracking)
