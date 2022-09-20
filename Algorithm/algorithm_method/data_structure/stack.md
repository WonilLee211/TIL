# stack

## 1. 스택이란

- LIFO(Last in, First out) : 후입선출, `나중에 입력된 데이터가 먼저 반환`되도록 설계한 메모리 구조
- 보통 웹의 undo 작업할 때 사용되는 자료구조
- DFS, 깊이우선탐색에 활용되는 자료구조

![Alt text](../../img/Data_stack.png)

### 구조

- 선형구조 : 자료간의 관계가 1:1 관계
- 비선형 구조 : 자료간의 관계가 1:N의 관계를 갖음(tree)

### 연산

- 삽입(push) : 저장소에 자료를 저장

- 삭제(pop) : 저장소에서 자료를 꺼낸다. 삽입한 자료의 역순으로 꺼냄

- `isEmpty` : 스택이 공백인지 아닌지 확인하는 연산.

- `peek` : 스택의 top에 있는 item을 반환하는 연산

- `top` : 스택에서 마지막에 삽입된 원소의 위치 
  
  <h6>출처 : https://ko.wikipedia.org/wiki/스택 </h6>
  ## 스택 구현 고려 사항

- 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점

- 스택의 크기를 변경하기 어렵다는 단점

### 저장소 동적 할당(연결리스트) ( 참고)

- 스택의 단점 보완
- 동적 연결 리스트를 이용하여 구현
- 구현이 복잡하지만 메모리를 효율적으로 사용한다는 장점

## 2. 파이썬에서 스택 구현

### 2.1 직접 구현1

```python
# 그냥 내장함수로 구현해도 된다.
s = []
def push(item):
  s.append(item)

def pop():
  if len(s) ==0:
    return # underflow
  else:
    return s.pop()
```

### 2.1 직접 구현2

```python
# 유한한 크기의 스택을 대상으로 더 빠른 연산
def push(item, size):
  global top
  top += 1

  if top == size:
    print('overflow')
  else:
    stack[top] = item

def pop():
  global top
  if top == -1:
    print('underflow')
    return 0
  else:
    top -= 1
    return stack[top + 1]

size = 10
stack = [0] * size
top = -1
```

### 2.2 리스트 이용

- 배열의 뒷 요소를 삭제할 때는 시간 복잡도가 deque와 차이 없음

```python
stack = []

stack.append('1st floor')
stack.append('2nd floor')
stack.append('3rd floor')
print(stack)

# ['1st floor', '2nd floor', '3rd floor']

stack.pop() # 3rd floor
stack.pop() # 2nd floor
stack.pop() # 1st floor
```

### 2.3 deque 클래스 활용
```python
from collections import deque
stack = deque()

stack.append('1st floor')
stack.append('2nd floor')
stack.append('3rd floor')
print(stack) 
# ['1st floor', '2nd floor', '3rd floor']

stack.pop() # 3rd floor
stack.pop() # 2nd floor
stack.pop() # 1st floor
```
