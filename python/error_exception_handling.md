# 에러/예외 처리(Error/Exception Handling)

# 목차

- 디버깅
- 에러와 예외
- 예외 처리
- 예외 발생시키기

---

# 디버깅

## 버그란?

- 명명유래 : 역사상 최초의 컴퓨터 버그는 Mark 2라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작

## 1. 디버깅의 정의

- 잘못된 프로그램을 수정하는 것
- 에러 메시지가 발생하는 경우
    - 해당하는 위치를 찾아 메세지를 해결
- 로직 에러가 발생하는 경우
    - 명시적 에러 메세지 없이 예상과 다른 결과가 나온 경우
        - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
        - 전체코드를 살펴봄
        - 휴식을 가져봄
        - 누군가에게 설명해봄

### 버그가 가장 많이 발생하는 곳

- 제어가 시작되는 시점 : 조건, 반복, 함수

### 디버깅 방법

1. print() 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
2. 개발환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
3. python tutor 활용( 단순 파이썬 코드인 경우)
4. 뇌컴파일, 눈디버깅

---

# 에러와 예외

## 1. 문법 에러(Sytax Error)

- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가르키는 캐럿(caret)기호(^)를 표시

### Invalid syntax

- 문법오류
    
    `while # SyntaxError: invalid syntax`
    

### assign to literal

- 잘못된 할당
    
    `5 = 3 # SyntaxError: cannot assign to literal`
    

### EOL(End Of Line)

- `print('hello # SystaxError: EOL while scanning string literal`

### EOF(End Of File)

- `print(     # SyntaxError: unexpected EOF while Parsing`

## 2. 예외(Exception)

- **실행 중에 감지되는 에러**
- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 예외는 여러 타입(Type)으로 나타나고, 타입이 메시지의 일부로 출력됨
    - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음

### ZeroDivisionError

- `10/0    # ZeroDivisonError: division by zero`

### NameError

- `print(name_error)    # NameError: name 'name_error' is not defined`

### TypeError

- `1 + '1'    # TypeError: unsupported operand type(s) for +: 'int' and 'str'`
- `round('3,5')    # TypeError : type str doesn't define __round__ method`
- `divmod()    # TypeError: divmod expected 2 arguments, got 0`
    
    ```python
    import random
    random.sample()
    # TypeError: sample() missing 2 required positional arguments: 'population' and 'k'
    ```
    
    ```python
    import random
    random.sample(1, 2)
    # TypeError: Population must be a sequence. For dicts or sets, use sorted(d).
    ```
    

### ValueError

- `int('3.5')    # ValueError: invalid literal for int() with base 10: '3.5'`
- `range(3).index(6)    # valueError: 6 is not in range`

### IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우

```python
empty_list = []
empty_list[2]
# IndexError: list index out of range
```

### KeyError - 해당 키가 존재하지 않는 경우

```python
song = {'IU' : '좋은날'}
song['BTS'] # KeyError: 'BTS'
```

### ModuleNotFoundError

```python
import ssafy #ModulNotFoundError: No module named 'ssafy'
```

### ImportError - 모듈 안에 존재하지 않는 클래스/함수를 가져오는 경우

```python
from random import sample
print(sample(range(3), 1)) # [1]
from random import samp
#ImportError: cannot import name 'samp' from 'random'(/usr/lib/python3.9/random.py)
```

### KeyboardInterrrupt - 임의로 프로그램을 종료하였을 때

```python
while True:
    continue

'''
Traceback (most recent call last):
  File "...", line 2, in <module>
    continue
KeyboardInterrupt
'''
```

### IndentationError - indentation이 적절하지 않은 경우

```python
for i in range(3):
print(i)    # IndentationError: expected an indented block

for i in range(3):
    print(i)
        print(i)
# IndentationError: unexpected an indented block
```

## 3. 파이썬 내장 예외(built-in-exceptions)

- 파이썬 내장 예외의 클래스 계층 구조
    - https://docs.python.org/ko/3/library/exceptions/html#exception-hierarchy
    ![Alt text](../../TIL/img/exception(built-in).PNG)

    ---
    

# 예외처리

- try문(statement)/ except절(clause)을 이용하여 예외 처리할 수 있음
- try 문
    - 오류가 발생할 가능성이 있는코드를 실행
    - 예외가 발생하지 않으면, except없이 실행 종료
- except문
    - 예외가 발생하면, except절이 실행
    - 예외 상황을처리하는 코드를 받아서 적절한 조치를 취함
- 예시
    
    ```python
    num = input('숫자 입력 :')
    print(int(num))
    '''
    숫자입력 :  안녕
    Traceback (most recent call last):
      File "...", line 2, in <module>
         print(int(num))
    ValueError: invalid literal for int() with base 10: '안녕'
    '''
    ```
    
    ```python
    try:
        num = input('숫자입력 : ')
        print(int(num))
    except:
        print('숫자가 아닙니다')
    
    '''
    숫자입력 :  안녕
    숫자가 아닙니다.
    '''
    try:
        num = input('숫자입력 : ')
        print(int(num))
    except ValueError:
        print('숫자가 아닙니다')
    
    '''
    숫자입력 :  안녕
    숫자가 아닙니다.
    '''
    ```
    

### 에러 메시지 처리(as)

- as 키워드를 활용하여 원본 에러 메세지를 사용할 수 있음
    - 예외를 다른 이름에 대입
    
    ```python
    [][1] # IndexError: list index out of range
    
    try:
        empty_list = []
        print(empty_list[-1])
    except IndexError  as err:
        print(f'{err}, 오류가 발생했습니다.')
    
    '''
    list index out of range, 오류가 발생했습니다.
    '''
    ```
    

### 복수의 예외 처리

- 100을 사용자가 입력한 값으로 나누고 출력하는 코드
    - 먼저 발생 가능한 에러가 무엇인지 예상해보시오.
    
    ```python
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
    ```
    
    - 문자열 입력 or 0 입력 : TypeError, ZeroDivisionError
    
    ```python
    try:
        num = input('100으로 나눌 값을 입력하시오 : ')
        100/int(num)
    except (ValueError, ZeroDivisionError):
        print('제대로 입력해줘.')
    
    try:
        num = input('100으로 나눌 값을 입력하시오 : ')
        100/int(num)
    except ValueError:
        print('숫자를 넣어주세요')
    except ZeroDivisionError):
        print('0으로 나눌 수 없습니다.')
    except:
        print('에러는 모르지만 에러가 발생했습니다.')
    # 가장 작은 범주가 위에 위치해야 함
    ```
    

### 예외 처리 종합

- try
    - 코드를 실행함
- except
    - try문에서 예외가 발생 시 실행함
- else
    - try문에서 예외가 발생하지 않으면 실행함
- finally
    - 예외 발생 여부와 관계없이 항상 실행함

### 활용 예시

- 파일을 열고 읽는 코드를 작성하는 경우
    - 파일 열기 시도
        - 파일 없는 경우 >> ‘해당 파일이 없습니다.’ 출력 `except`
        - 파일이 있는 경우 >> 파일 내용을 출력  `else`
    - 해당 파일 읽기 작업 종료 메시지 출력  `Finally`

```python
try:
    f = open('nooofile.txt')
except FileNotFoundError:
    print('해당 파일이 없습니다.')
else:
    print('파일을 읽기 시작합니다.')
    print(f.read())
    print('파일을 모두 읽었습니다.')
finally: # 항상 실행
    print('파일 읽기는 종료합니다.')

'''해당 파일이 없는 경우
해당 파일이 없습니다.
파일 읽기는 종료합니다.
'''
'''파일이 존재하는 경우
파일 읽기 시작합니다.
파일을 모두 읽었습니다.
파일 읽기는 종료합니다.
'''
```