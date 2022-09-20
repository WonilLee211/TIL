# 비트 연산자

## 비트연산자 기호

1. & : 비트 단위로 and 연산
2.  | : 비트 단위로 or 연산
3. << : 쉬프트 연산자. 피연산자의 비트 열을 왼쪽으로 이동시킨다. ( 2진수로 만듬)
    1.  곱하기 2한것과 같음
    2. 1<<2 : 100(2)
4. >> : 쉬프트 연산자. 피연산자의 비트 열을 오른쪽으로 이동시킨다.
    1. 나누기 2한 것과 같음
    2. 100>>2 : 1(2) 

## << 연산자

- 1 << n : 2^n 즉, 원소가 n개 일 경우의 모든 부분집합의 수

## & 연산자

- i & (1<<j) : i의 j번째 비트가 1인지 아닌지 검사
- 십진수 & 십진수 >> 이진수로 변환해서 각 자리 비교

```makefile
7 : 0111
& 
5 : 0101
결과 ; 0101 >> 5 반환
```

## <mark>간결하게 부분집합을 생성하는 법</mark>

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # n : 원소의 개수

for i in range(1<<n): # 1<<n : 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번 비트가 1인 경우
            print(arr[j], end =", ") # j번째 원소 출력
    print()
print()
```

### 부분 집합 합 문제

- 실제 10개의 정수를 입력 받아 부분 집합의 합이 0이 되는 것이 존재하는지 계산하는 함수

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

        print(f"#{test_case} {subset(numbers)}")
```