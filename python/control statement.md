# 제어문(control statement)

- **종류**
  1. 조건문
  2. 반복문
- 위에서부터 아애로 차례대로 명령
- 순서도(flowchart)로 표현 가능

---

## 1. 조건문(conditional statement)

### 1.1 조건문 기본

- 참거짓을 판단할 수 있는 조건식과 함께 사용
- if , elif, else
- num의 값의 홀수/짝수 여부를 출력

```python
if num%2:
    print('홀수')
else:
    print('짝수')
```

### 1.2 복수 조건문

- elif 활용
- 동시에 비교하는 게 아니라 순차적으로 비교 판단

### 1.3 중첩 조건문

- 다른 조건문에 중첩되어 사용될 수 있음
  
  - 들여쓰기 유의하여 작성할 것
    
    ```python
    if 조건:
      # 코드블럭
      if 조건:
          # 코드블럭
    else:
      # 코드블럭
    ```

### 1.4 조건 표현식

```python
num = 2
if num%2:
    result = '홀수'
else:
    result = '짝수'
print(result)
```

```python
num = 2
result = '홀수' if num % 2 else '짝수'
print(result)
```

---

## 2. 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
- 종류
  1. while문
     1. 종료조건에 해당하는 코드를 통해 반복문 종료
  2. for 문
     1. 반복가능한 객체를 모두 순회하면 종료
  3. 반복 제어
     1. break, continue, for-else

### 2.1 while문

- 복합연산자(In-place Operator)
  
  - 연산과 할당을 합쳐 놓은 것
    
    ```python
    a = 0
    while a < 5:
      print(a)
        a += 1
    print('끝')
    ```

### 2.2 for문

- 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소를 모두 순회

- <mark>**iterable</mark>**
  
  - 순회할 수 있는 자료형
  - string, list, dict, tuple, range, set 등
  - 순회형 함수(range, enumerate)

- **딕셔너리 순회**
  
  - 기본적으로 key를 순회하며 반환
  - 추가메서드
    - keys() : key로 구성된 결과
    - values() : value로 구성된 결과
    - items() : (key, value)의 튜플로 구성된 결과

- enumerate 순회
  
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    
    ```python
    members = ['민수', '영희', '철수']
    for idx, member in enumerate(members):
      print(idx, member)
    
    '''
    0 민수
    1 영희
    2 철수
    '''
    ```
  
  - enumerate( interable, start = 0)
    
    ```python
    members = ['민수', '영희', '철수']
    list(enumerate(members, start = 1)
    # [(1, '민수'), (2, '영희'), (3, '철수')]
    ```

- **line comprehension**
  
  - `[code for 변수 in iterable if 조건식]`

- **dictionary comprehension**
  
  - `{key:value for 변수 in iterable if 조건식}`

### 2.3 반복문 제어

- `break` : 반복문을 종료
- `continue` : continue 이후의 코드블럭은 수행하지 않고 다음 반복을 수행
- `for-else` : 끝까지 반복문을 실행한 이후에 else문 실행
  - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
- `pass` : 아무것도 하지 않음.(문법적으로 필요하지만, 할 일이 없을 때 사용)
- for -break - else 연습해보기