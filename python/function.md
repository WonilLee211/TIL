목차

- 함수기초
- 함수의 결과값(output)
- 함수의 입력(input)
- 함수의 범위(scope)
- 함수의 문서화(doc-string)
- 함수 응용
---
# 함수

- 특징
    1. Decomposition(분해)
    2. Abstraction(추상화)
1. Decomposition
    - 기능 분해와 재사용 가능
2. abstraction
    - 가독성을 높힘
    - 내부 구조를 잘 몰라도 잘 사용하기만 하면 됨
---
## 1. 함수의 기초

### 1.1 함수의 종류

1. 내장함수 : 파이썬에 기본적으로 포함된 함수
2. 외장함수 : import문을 통해 사용, 외부 라이브러리에서 제공하는 함수
3. 사용자 정의 함수 : 직접 사용자가 만든 함수

### 1.2 함수의 정의

- 특정한 기능을 하는 코드 조각

### 1.3 함수의 기본 구조

- 선언과 호출
    - def키워드로 선언
    - function body에 코드 작성
    - docsting은 첫번째 문장에 `'''`
    - parameter 넘겨줄 수 있음
    - return을 통해 결괏값 전달
- 입력
- 문서화
- 범위
- 결과값
---
## 2. 함수의 결과값(output)

- 값에 따른 함수의 종류
    1. void fucntion : return이 없는 경우 None반환 후 종료
    2. value returning function
        1. 튜플을 활용한 두 개 이상의 값 반환
        
        ```python
        def minus_and_product(x, y):
            return x-y, x*y
        ```
        
---
## 3. 함수의 입력(intput)

- Parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수
- Argument : 함수를 호출할 때, 넣어주는 값
    1. 필수 argument : 반드시 전달되어야 하는 argument
    2. 선택 argument : 값을 전달하지 않아도 되는 기본값이 전달

### 3.1 positional Arguments

- 기본적으로 함수 호출 시 argument는 위치에 따라 함수에 전달됨

```python
def add(x, y):
    return x + y

add(2, 3) # x = 2, y = 3
# 5
```

### 3.2 keyword Arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- keyword argument 사용 후 postional argument 사용할 수 없음

```python
def add(x, y):
    return x + y

add(x=2, y=5) # 7
add(2, y =5) # 7
add(x=2, 5) # 에러 발생
```

### 3.3 Default Arguments Values

- 기본값을 지정하여 함수 호출 시 argument값을 설정하지 않도록 함
    - 정의된 것 보다 더 적은 개수의 argument들로 호출될 수 있음
    
    ```python
    def add(x, y=0):
        return x + y
    
    add(2) # add(2, y = 0)
    add(2, 4) # 6
    ```
    

### 3.4 가변인자(*args)

- 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용
- 몇 개의 PA를 받을지 모르는 함수를 정의할 때 유용
- 언팩킹연산자 or 애스터리스크(asterisk) : `*`

```python
def add(*args):
    for arg in args:
        print(arg)
```

### 3.5 패킹/언패킹

- 가변 인자를 이해하기 위해서는 패킹, 언패킹을 이해해야 함.
- 패킹 : 여러개의 데이터를 묶어서 변수에 할당하는 것
    - `numbers = (1, 2, 3 , 4, 5)`
- 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나눵서 할당하는 것
    
    ```python
    numbers = (1, 2, 3, 4, 5)
    a, b, c, d, e = numbers
    ```
    
    - `언패킹 시, 변수의 개수와 할당하고자 하는 요소의 개수가 동일해야 함.`
    
    ```python
    numbers = (1, 2, 3, 4, 5)
    a, b, c, d, e, f = numbers
    # ValueError : not enough values to unpack
    
    a, b, *rest = numbers # 1, 2를 제외한 나머지를 rest에 대입
    a, *rest, e = numbers # 1, 5를 제외한 나머지를 rest에 대입
    print(rest) # [2, 3, 4]
    ```
    

### 3.6 <mark>Asterist(`*`)와 가변인자</mark>

- `*` 는 시퀀스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자
- 튜플이나 리스트 언패킹에 사용

```python
def func(*args):
    print(args)
    print(type(args))

func(1, 2, 3, 'a', 'b')
'''
(1, 2, 3, 'a', 'b')
<class 'tuple'>
'''
```

### 3.7 가변 키워드 인자(**kwargs)

- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
- **kwargs는 **딕셔너리로 묶여 처리**되며, parameter에 **를 붙여 표현

```python
def family(**kwargs): 
    for key, value in kwargs.items():
        print(key, ":", value)
family(father = '아부지', mother = '어머니' , baby = '아기')
## 여러 개로 들어오는 정보를 딕셔너리로 만들어줄 뿐이고 매개변수를 형변환한다는 말은 아님.
## *kwargs는 매개변수명도 저장해야하고 뒤에 값도 저장해야하니 딕셔너리형태로 모여지는 것
'''
father : 아부지
mother : 어무니
baby : 아기
'''
```

- 가변인자와 가변 키워드 인자를 동시에 사용할 수 있을까?
    
    ```python
    def print_family_name(*parents, **pets):
        print('아버지 :', parents[0])
        print('어머니 :', parents[1])
        if pets:
            print('반려동물들..')
            for title, name in pets.items():
                print('{} : {}'.format(title, name))
    
    print_family_name('아부지','어무이', dog = '멍멍이', cat = '냥냥이')
    '''
    father : 아부지
    mother : 어무니
    반려동물들...
    dog : 멍멍이
    cat : 냥냥이
    '''
    ```
    
---
## 4. Python의 범위(Scope)

### 4.1 Python의 범위

- scope
    - local scope : 함수 코드 내부에서만 참조 가능
    - global scope : 그 외의 공간. 코드 어디에서든 참조할 수 있는 공간
- variable
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

### 4.2 변수 수명주기(lifecycle)

- 변수는 각자의 수명 주기(lifecycle)존재
1. built-in scope : 파이썬이 실행된 이후부터 영원히 유지
2. global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    
    ```python
    def func():
        a = 20
        print('local', a)
    
    func()
    print('global', a) # NameError : name 'a' is not defined
    ```
    

### 4.3 이름 검색 규칙(name resolution)

- 파이썬에서 사용되는 이름(식별자)는 이름공간에 저장되어 있음
- <mark>LEGB Rule</mark>
    1. Local scope
    2. Enclosed scope : 이중 def에 대해서 바깥 구역
    3. Global scope 
    4. Built-in Scope : ex) print()
    - <mark>함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음</mark>
        
        
    - 예시
        
        ```python
        print(sum) # <built-in function sum>
        print(sum(range(2))) # 1 built-in scope에서 sum을 불러왔음
        
        sum = 5 # global scope에 sum이 저장됨
        
        print(sum) # 5 global scope에서 sum을 불러옴
        print(sum(range(2))) # TypeError : 'int' object is not callable
        											# bilt-in scope으로 넘어가지 않고 global에서 찾고 탐색 끝남
        
        ## LEGB 순의 탐색 순서
        ```
        
    
    ```python
    # 예시
    a = 0
    b = 1
    def enclosed():
        a = 10
        c = 3
        def local(c):
            print(a, b, c)
        local(a, b, c)
        print(a, b, c)
    enclosed()
    
    print(a, b)
    '''
    10 1 300
    10 1 3
    0 1
    '''
    ```
    

### 4.4 global 문

- 현재 코드 블럭 전체에 적용되어 나열된 식별자(이름)이 global variable임을 나타냄

```python
# 함수 내부에서 글로벌 변수 변경하기
# 함수에서 변수를 변경하려고 한다면 변수가 글로벌에서 생성된 것이어야 함.
a = 10
def func1():
    global a
    a = 3

print(a)    # 10
func1()
print(a)    # 3
```

- <mark>주의</mark>
    - global에 나열된 식별자는 같은 코드블럭에서 global 앞에 등장할 수 없음
        
        ```python
        # global 주의사항
        a = 10
        def func1():
            print(a)
            global a
            a = 3
        
        print(3)
        func()
        print(a)
        # SyntaxError : name 'a' is used prior to global declaration
        ```
        
    - global에 나열된 이름은 **parameter, for 루프 대상, 클래스/함수 정의** 등으로 정의되지 않아야 함
        
        ```python
        # global 주의사항
        a = 10
        def func1(a):
            global a
            a = 3
        
        print(a)
        func(3)
        print(a)
        # SyntaxError : name 'a' is parameter and global
        ```
        

### 4.5 nonlocal

- global 을 제외하고 가장 가까운 scope의 변수를 연결하도록 함
- global과 달리 이미 존재하는 이름과 연결만 가능

```python
a = 0
def func1():
    a = 1
    def func2():
        nonlocal a
        a = 2
    func2()
    print(a) # 2
func1()
print(a) # 0
```
---
## 5. 함수 응용

### 5.1 내장함수(built-in Functions)

- map(function, iterable) : iterbale 데이터의 모든 요소를 함수에 적용하고 map object로 반환
- filter(function, iterable) : iterable 데이터의 모든 요소를 함수에 적용하고 True인 것만 filter object로 반환
    
    ```python
    def odd(n):
        return n % 2
    numbers = [1, 2, 3]
    result = filter(odd, numbers)
    print(list(result)) # [1, 3]
    ```
    
- zip(*iterables) : 복수의 iterable을 모아 **튜플**을 원소로 하는 zip object로 반환
    
    ```python
    girls = ['jane', 'ashley']
    boys = ['justin', 'eric']
    pair = zip(girls, boys)
    print(list(pair)) # [('jane','justin'), ('ashley','eric')]
    ```
    
- lambda[ parameter] : 표현식 : 무기명함수며 일회성 함수. 표현식을 계산한 결과값을 반환
    
    ```python
    #삼각형 넓기 구하기
    triangle_area = lambda b, h : 0.5 * b * h
    
    print(triangle_area(5,6)) # 15.0
    ```
    
- 재귀 함수(recursive function) : 자기 자신을 호출하는 함수
    - 1 개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
    
    ```python
    #factorial 작성
    def factorial(n):
        if n==0 or n==1 : return: 1
        return n * factorial(n-1)
    
    print(factorial(4)) # 24
    ```
    
    - <mark>**주의</mark>**
        - 메모리 스택이 넘치면 프로그램 동작 안함
        - 파이썬에서 최대 재귀 깊이 1000번(이상은 Recursion Error)
        - 입력값이 커질수록 연산속도가 오래 걸림
- 표현식과 문장의 차이
    
    print로 찍었을 때 값이 나오면 표현식이라고 할 수 있다.
    
    함수 호출은 표현식이다.
    
    함수 자체는 문자다.
    
---
## 6. 모듈

- 모듈과 패키지
    - 모듈 : 다양한 기능을 하나의 파일로 모은 묶음
    - 패키지 : 다양한 파일을 하나의 폴더로 모은 묶음
- 파이썬 표준 라이브러리
    - 라이브러리 : 다양한패키지를 하나로 모은 묶음. 주도권이 나한테 있는 느낌
    - 프레임워크 : 라이브러리랑 비슷하지만 주도권이 나한테 없는 느낌…
        - pip : 이것을 관리하는 관리자
- 가상환경
    - 패키지의 활용 공간
- 유용한 패키지와 모듈
- 사용자 모듈과 패키지

### 6.1 모듈과 패키지

- 모듈 : 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또다른 서브 패키지를 포함
- 불러오기
    
    ```python
    import module
    from module import var, function, Class
    from module import *
    
    from package import module
    from package.module imoport var, function, Class
    ```
    

### 6.2 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장함수
    - `https://docs.python.org/ko/3/library/index/html`
- 파이썬 패키지 관리자(pip)
    - PyPI(Python Package index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
    - 설치 : `$ pip install package_name`
    - 삭제 : `$ pip uninstall package_name`
    - 목록 보기 : `$pip list`
    - 특정 패키지 정보 : `$ pip show package_name`
    - 패키지 관리하기 :
        
        ```python
        $ pip freeze > requirements.txt
        # 패키지 목록을 관리하고
        $ pip install -r requirements.txt
        # 설치할 수 있음
        ```
        

### 6.3 사용자 모듈과 패키지

- 패키지 : 여러 모듈이나 패키지로 구조화되어 있음
- 모든 폴더는 `__init__.py`를 만들어 패키지로 인식
    - Python3.3부터는 없어도 불러쓸 수 있지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성하는 것을 권장
- 패키지 만들기
    - 폴더구조
    
    ```python
    my_package/
        __init__.py
        check.py
        calculator/
            __init__.py
            tools.py
    ```
    
    - [tools.py](http://tools.py) 파일만들기
    
    ```python
    # calculator/tools.py
    def add(num1, num2):
        return num1 + num2
    
    def minus(num1, num2):
        return num1 - num2
    ```
    
    - 모듈 활용하기
    
    ```python
    from calculator import tools
    
    print(dir(tools)) # tools에 어떤 변수와 메서드를 가지고 있는지 나열
    '''
    [ ... , 'add', 'minus']
    print(tools.add(3, 5)) # 8
    ```
    

### 6.4 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는경우 pip를 통해 설치해야 함.
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음.
    
    이때 가상환경을 만들어 프로젝트 별로 독립적인 패키지를 관리할 수 있음
git bash에서
1. 가상환경 생성 `$ python -m venv <폴더명>`
2. 가상환경 활성화(window) : `C:\> <venv> \Scripts\activate.bat`
3. 가상환경 활성화 (git bash) : `$ source venv/Scripts/activate`
    1. 비활성화 : `$ deactivate`