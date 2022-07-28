# OOP 객체지향 프로그래밍 및 에러처리

## 목차

- **객체지향 프로그래밍(OOP)**
    - 객체 지향 프로그래밍이란?
- OOP 기초
    - 객체 / 인스턴스 / 클래스
    - 클래스
    - 메서드
- **객체 지향의 핵심개념**
    - 추상화
    - 상속
    - 다형성
    - 캡슐화
- **에러와 예외**

---

# OOP 객체 지향 프로그래밍

- 컴퓨터 프로그래밍의 페러다임 중 하나
- 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위인 “객체”들의 모임을 파악하고자 하는 것
- 각각의 객체는 메세지를 주고받고, 데이터를 처리할 수 있다.
- 

## 1. 객체지향 프로그래밍이란?

- <mark>**객체 : 정보와 행동**으로 나뉜다.</mark>
    - 변수에 행동은 못 들어간다. 변수와 함수가 묶인 것을 객체라고 한다.
- **여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 프로그램을 파악하는 방법**
- 예시
    - 콘서트
        - 가수 객체
        - 감독 객체
        - 관객 객체

### 절차지향 프로그래밍이 사라진 이유

- 데이터와 함수의 서로 복잡하게 엮여있음
- 이로 인해 수정 및 보수가 어려움
- 현실세계가 너무 복잡하다

### 객체지향 프로그래밍

- 객체, object의 각각의 기준에 맞춰서 데이터, 함수를 분리하고 묶음
- 추상화된 구조(인터페이스)
    - 추상화 : 복잡한 걸 숨기고 필요한 것만 들어내는 것

### 객체지향 장단점

장점

1. 클래스 단위로 모듈화시켜서 개발할 수  있음
    1. 많은 인원이 참여하는 대규호 소프트웨어 개발에 적합
    2. 필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 쉬움

단점

1. 설계 시 노력과 시간이 필요
    1. 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
    2. 알고리즘 문제를 풀 때는 잘하지 않음
2. 실행 속도 상대적으로 느림
    1. 절차지향 프로그래밍이 컴퓨터의 처리 구조와 비슷해서 실행 속도가 빠름

---

# OOP 기초

## 1. 객체(컴퓨터 과학)

- <mark>속성(변수)과 행동(메서드)으로 구성된 모든 것</mark>
- 컴퓨터 과학에서 객체 또는 object는 **클래스에서 정의한 것을 토대로 메모리에 할당된 것**
- 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미
- 변수, 자료구조, 메서드가 될 수도 있음

### 예시

클래스( 설계도 ) - 가수

객체(실제 사례) - 이찬혁

### 객체와 인스턴스

클래스로 만든 객체(어떤 클래스의 객체)를 인스턴스라고 한다.

- 이찬혁은 객체이다 ( O ) ( 정보 + 행동이면 전부 객체이다)
- 이찬혁은 인스턴스다 ( X ) ( 특정 타입의 인스턴스라고 해야 한다.)
- 이찬혁은 가수의 인스턴스다( O ) ( 어떤 클래스의 인스턴스이다)

클래스는 list와 같은 타입이다…

### 예시

[1, 2, 3] . sort( ) / 리스트 . 정렬( ) / 객체 . 행동( ) / 인스턴스.인스턴스 메서드

### 객체와 인스턴스

- 타입과 실제사례
- [1,2,3], [1], [] : 전부 객체이며 리스트타입(클래스)의 인스턴스
- 객체(object)는 특정 타입의 인스턴스(instance)이다.

### 객체의 특징

1. 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가? **클래스 종류**
2. 속성(attribute) : 어떤 상태(데이터)를 가지는가? **변수**
3. 조작법(method) : 어떤 행위(함수)를 할 수 있는가? **메서드**

---

# 객체와 클래스 문법

## 1. 기본 문법

```python
# 클래스 정의
class MyClass:
		pass
# 인스턴스 생성
my_instance = MyClass()
# 메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute
```

### <mark>명명규칙</mark>

- 파스칼 케이스 : 클래스 명명할 때 사용 - 단어 조합일 때 각 단어 앞 대문자로 표현
- 스내이크 케이스 : 함수를 명명할 떄 사용 - 단어 조합일 때 구분자로 `_` 사용

## 2. 클래스와 인스턴스

- 객체의 설계도(클래스)를 가지고 객체(인스턴스)를 생성한다.
- 클래스 : 객체들의 분류/ 설계도(class)
- 인스턴스 : 하나하나의 실체/ 예(instance)

```python
class Person:
		pass

print(type(Person)) # <class 'type'>

person1 = Person()
print(isinstance(person1, Person)) # 펄슨 1 객체가 펄슨 클래스의 인스턴스인가?
# True
print(type(person1)) # <class '__main__.Person'>
```

## 3. 객체 비교하기

- `==`
    - 동등한(equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인한 건 아님
- `is`
    - 동일한(identical)
    - 두 변수가 동일한 객체를 가르키는 경우 True
    
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    
    print(a == b, a is b) # True False
    
    a = [ 1, 2, 3]
    b = a
    
    print(a == b, a is b) # True True
    ```
    

---

# OPP 속성

## 1. 속성

- 특정 데이터 타입/ 클래스의 **객체들이 가지게 될 상태/데이터**를 의미
- 종류
    1. 클래스 변수
    2. 인스턴스 변수
    
    ```python
    class Person:
    		blood_color = 'red' # 클래스 변수
    		population = 100 # 클래스 변수
    
    		def __init__(self, name): # 클래스 선언할 때 이름이라는 문자열을 arg로 전달해야 함
    				self.name = name # 인스턴스 변수
    
    person1 = Person('지민') #
    prnit(person1.name) # 지민
    ```
    

## 2. 인스턴스 변수

- 인스턴스 변수란?
    - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
    - 각 인스턴스들의 고유한 변수
- 생성자 메서드(`__init__`)에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당
    
    ```python
    class Person:
    		def __init__(self, name): # 인스턴스 변수 정의
    				self.name = name
    
    john = Person('john') # 인스턴스 변수 저장
    print(john.name) # john # 인스턴스 변수 접근
    john.name = 'John Kim' # 인스턴스 변수 할당
    print(john.name) # John Kim
    ```
    

## 3. 클래스 변수

### 클래스 변수

- **한 클래스의 모든 인스턴스가 공유하는 값**을 의미
- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
- 예) 특정 사이트의 User 수 등의 클래스 변수를 사용해야 함
- 클래스 선언 내부에서 정의
- <classname>, <name>으로 접근 및 할당
    
    ```python
    class Circle:
        pi = 3.14 # 클래스 변수 정의
    
    		def __init__(self, r):
    				self.r = r #  인스턴스 변수
    
    c1 = Circle(5)
    c2 = Circle(10)
    
    print(Circle.pi) # 3.14
    print(c1.pi) # 3.14
    print(c2.pi) # 3.14
    
    Circle.pi = 5
    print(Circle.pi) # 5
    print(c1.pi) # 5
    print(c2.pi) # 5
    ```
    

### 클래스 변수 활용 ( 사용자 수 계산하기)

- 사용자가 몇 명인지 확인하고 싶다면?
    - 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정하면 됨
    
    ```python
    class Person:
        count = 0
        # 인스턴스 변수 설정
        def __init__(self, name):
            self.name = name
            Person.count += 1
    person1 = Person('이찬혁')
    person2 = Person('아이유')
    
    print(Person.count) # 2
    ```
    
    - <mark>클래스 변수 변경 : `클래스.클래스 변수` 형식으로 변경</mark>
        
        ```python
        class Circle:
            pi = 3.14 # 클래스 변수 정의
        
        		def __init__(self, r):
        				self.r = r #  인스턴스 변수
        
        c1 = Circle(5)
        c2 = Circle(10)
        
        print(Circle.pi) # 3.14
        print(c1.pi) # 3.14 문법상 자동으로 인스턴스 변수가 없으면 클래스변수를 찾는다
        print(c2.pi) # 3.14
        ```
        
        ```python
        Circle.pi = 5 # 클래스 변수 변경
        print(c1.pi) # 5
        print(c2.pi) # 5
        ```
        
        ```python
        c1.pi = 5 # 인스턴스 변수 변경
        print(c1.pi) # 5
        print(c2.pi) # 3.14
        ```
        

---

# OOP 메서드

- 특정 데이터 타입/ 클래스의 객체에 공통적으로 적용 가능한 행위(함수)

```python
class Person:
    def talk(self):
        print('안녕')

    def eat(self, food):
        print(f'{food}를 냠냠')
person1 = Person()
person1.talk() # 안녕
person1.eat('피자') # 피자를 냠냠
person1.eat('치킨') # 치킨를 냠냠
```

## 메서드 종류

### 인스턴스 메서드

- 인스턴스의 영역
- `self` 파라미터 필수
- 객체를 통해 접근할 수 있음

### 클래스 메서드

- `self` 필요없음
- cls 파라미터 필요함.
- class 매서드 디코레이터 필요함
- 클래스를 통해서 접근 가능

### 정적 메서드

- 나머지
- 아규먼트로서 통과되는 변수에 접근 가능

## 1. 인스턴스 메서드

- 인스턴스 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫 번째 인자로 인스턴스 자기자신(self)이 전달됨.

### self

- 인스턴스 자기자신
- 파이썬에서 인스턴스 메서드 호출 시 첫 번째 인자로 인스턴스 자신이 전달되게 설계
- 암묵적인 규칙

### 생성자(constructor) 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값 설정
    - 인스턴스 생성
    - `__init__` 메서드 자동 호출
    
    ```python
    class Person:
        def __init__(self, name):
            print(f'인스턴스가 생성되었습니다. {name}')
    
    person1 = Person('지민') # 인스턴스가 생성되었습니다. 지민
    ```
    

### 매직 메서드

- Double uderscore(__)가 있는 메서드는 특수한 동작을위해 만들어진 메서드.
- 스페셜 메서드라고도 불림
- 특정 상황에서 자동으로 불리는 메서드

```python
- __str__(self), __len(self)__, __repr__(self)
- __lt__(self, other), __le__(self, other), __eq__(self, other)
- __gt__(self, other), __ge__(self, other), __ne__(self, other)
```

- 객체의 특수 조작 행위를 지정( 함수, 연산자 등)
- 예시
    - 객체의 특수 조작 행위를 지정(함수, 연산자 등)
        - **str** : 해당 객체의 출력 형태를 지정
            - 어떤 인스턴스를 출력하면 `__str__`의 return 값이 출력
        - `__gt__` : 부등호 연산자(> , greater than)

```python
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
    def __str__(self): # 인스턴스 메서드
        return f'[원] radius : {self.r}'
    def __gt__(self, other): # 인스턴스 메서드
        return self.r > other.r

c1 = Circle(10)
c2 = Circle(1)

print(c1) # [원] radius: 10
print(c2) # [원] radius: 1
print(c1 > c2) # True
print(c1 > c2) # False
```

### 소멸자(destructor) 메서드

- 인스턴스 객체가 소멸되기 직전에 호출되는 메서드

```python
class Person:
    def __del__(self):
        print('인스턴스가 사라졌습니다')

person1 = Person()
del person1 # 인스턴스가 사라졌습니다.
```

## 2. 클래스 메서드

- 클래스가 사용할 메서드
- 클래스 변수를 사용할 때 정의해서 사용한다( 안쓰면 정의할 필요 없음)
- @classmethod 데코레이터 사용하여 정의
- 호출시 첫 번째 인자로 클래스 cls가 전달됨(인스턴스 메서드에 self같은 느낌)

```python
class Person:
    count = 0
    # 인스턴스 변수 설정
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_population(cls):
					print(f'인구수는 {cls.count}입니다.')

person1 = Person('이찬혁')
person2 = Person('아이유')
print(Person.count) # 인구수는 2입니다.
```

- 

### 데코레이터

- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 적용 되기 떄무에 작성 순서가 중요

- 데코레이터 없이 함수 꾸미기
    
    ```python
    def hello:
        print('hello')
    
    #데코레이팅 함수
    def add_print(original): # 파라미터로 함수를 받는다
        def wrapper(): # 함수 내에서 새로운 함수 선언
            print('함수 시작')
            original()
    	        print('함수 끝')
        return wrapper # 함수를 return 한다.
    
    add_print(hello)()
    print_hello = add_print(hello)
    print_hello()
    # 함수 시작
    # hello
    # 함수 끝
    ```
    

- <mark>데코레이터</mark>

```python
# 데코레이팅 함수
def add_print(original): # 파라미터로 함수를 받는다
    def wrapper(): # 함수 내에서 새로운 함수 선언
        print('함수 시작')
        original()
	      print('함수 끝')
    return wrapper # 함수를 return 한다.

@add_print
def print_hello():
    print('hello')

print_hello()
# 함수 시작
# hello
# 함수 끝
```

### 클래스 메서드와 인스턴스 메서드

- 클래스 메서드 > 클래스 변수 사용
- 인스턴스 메서드 > 인스턴스 변수 사용
- 둘 다 사용하고 싶다면?
    - 클래스는 인스턴스 변수 사용이 불가능
    - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용 가능
    

## 3. 스태틱 메서드

### 스태틱 메서드

- 인스턴스 변수, 클래스 변수를 전혀 다루지 않은 메서드

### 언제사용하는가?

- 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용

### 특징

- 인스턴스 변수, 클래스 변수를 사용하지 않기 때문에 객체 상태나 클래스 상태를 수정할 수 없음
- @staticmethod 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 이름 공간에 귀속됨
- 주로 해당 클래스로 한정하는 용도로 사 용

```python
class MyClass:

    @staticmethod
    def static_method(arg1, ..):

MyClass.static_method(..)
```

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @staticmethod
    def check_rich(money): # 스태틱은 cls, self 사용 X
        return money > 10000

person1 = Person('아이유')
person2 = Person('이찬혁')
print(Person.check_rich(1000000)) # True, 스태틱은 클래스로 접근 가능
print(person1.check_rich(1000000)) # True, 스태틱은 클래스로 접근 가능
```

## 4. 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

```python
# Person 정의
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1. = Person()
p1.talk() # unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk() # unknown
p2.name = 'Kim'
p2.talk() # Kim
```

## 메서드 정리

- 인스턴스 메서드 : 호출한 인스턴스를 의미하는 self 매개변수를 통해 인스턴스를 조작
    
    
- 클래스 메서드 : 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
    
    
- 스태틱 메서드 : 클래스 변수나 인스턴스 변수를 사용하지 않는경우 사용

```python
class MyClass:
    def method(self):
        return 'instance method', self

		@classmethod
    def classmethod(cls):
        return 'class method', cls

    @staticmethod
    def staticmethod():
        return 'static method'

```

- 인스턴스 메서드를 호출한 결과

```python
obj = MyClass()

print(obj.method()) # ('instance method', <__main__.MyClass at 0x185fd086a00>)
print(MyClass.method(obj)) # ('instance method', <__main__.MyClass at 0x185fd086a00>)
```

- 클래스 자체에서 각 메서드를 호출하는 경우

```python
print(MyClass.classmethod()) # ('class method', __main__.Mycalss)
print(MyClass.staticmethod()) # static method
MyClass.method() # method() missing 1 required positional argunment: 'self'
# 클래스 자체에서 인스턴스 메서드를 호출할 수 없음 !!!
```

- 인스턴스에서 클레스 매서드와 스태틱 메서드 모두 접근할 수 있음

```python
print(obj.classmethod()) # ('class method', <class '__main__.MyClass'>)
print(MyClass.classmethod()) # ('class method', <class '__main__.MyClass'>)
print(obj.staticmethod()) # static method
```

---

# 객체 지향의 핵심 개념

- <mark>상추캐다 외우기</mark>

## 4가지 핵심 개념

1. 추상화 : 복잡한거 숨기고 필요한 거 나타냄
2. 상속 : 부모클래스 자식클래스 관계 (재사용을 위한)
3. 다형성 : 이름은 같은데 동작이 다른것
4. 캡슐화 : 민감한 정보를 숨기는 것

## 1. 추상화

- 복잡한 것은 숨기고 필요한 것만 들어내기
- 현실세계를 프로그램 설계에 반영
    
    ```python
    # 학생(student)을 표현하기 위한 클래스를 생성합니다.
    class Student:
        def __init__(self, name. age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa
    
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
        def study(self):
            self.gpa += 0.1
    
    class professor:
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
        def teach(self):
            self.age += 1
    
    class Person:
        def __init__(self, name. age):
            self.name = name
            self.age = age
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
    
    ```
    

---

## 2. 상속

- 상속이란 : 두 클래스 사이 부모 - 자식 관계를 정립하는 것
- 클래스는 상속이 가능함 : **모든 파이썬 클래스는 object를 상속받음**

```python
class ChildClass(ParentClass):
   pass
```

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

```python
class Person:
    def __init__(self, name. age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Student(Person):
    def __init__(self, name. age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

class professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

p1 = professer('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.
```

### 상속관련 함수와 메서드

- isinstance(object, classinfo) : classinfo의 instance거나 <mark>subclass</mark> 인 경우 True

```python
print(isinstance(p1, Person)) # True
print(isinstance(p2, Person)) # True
```

- issubclass(class, classinfo)
    - class가 classinfo의 subclass면 True
    - classinfo는 클래스 객체의 튜플(?)일 수 있으며, classinfo의 모든 항목을 검사
    
    ```python
    print(issubclass(bool, int)) # True
    print(issubclass(float, int)) # False
    print(issubclass(Professor, Person) # True 프로페서가 펄슨을 상속받았음
    print(issubclass(Professor, (Person, Student))) # True(?)
    ```
    
- super() : 자식클래스에서 부모 클래스의 변수를 사용하고 싶은 경우
    
    ```python
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email
    
    class student(Person):
        def __init__(self, name, age, number, email, student_id):
            self.name = name
            self.age = age
            self.number = number
            self.email = email
            self.student_id = student_id
    ```
    
    ```python
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email
    
    class student(Person):
        def __init__(self, name, age, number, email, student_id):
            #Person 클래스
            super().__init__(name, age, number, email)
            self.student_id = student_id
    ```
    

- 상속정리
- 파이썬의 모든 클래스는 object로부터 상속됨
- super()를 통해 부모클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 **이름 공간은 인스턴스, 자식 클래스, 부모클래스 순으로 탐색**

### 다중상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속받는 모든 클래스의 요소를 활용 가능함
- 중복된 속석이나 메서드가 있는 경우 상속 순서에 의해 결정됨
    
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
        def greeting(self):
            return f'안녕, {self.name}'
    
    class Mom(Person):
        gene = 'XX'
    
        def swim(self):
            return '엄마가 수영'
    
    class Dad(Person):
        gene = 'XY'
    
        def walk(self):
            return '아빠가 걷기'
    
    class FirstChild(Dad, Mom):
        def swim(self):
            return '첫째가 수영'
        def cry(self):
            return '첫째가 응애'
    
    baby1 = FirstChild('아가')
    print(baby1.cry()) # 첫째가 아가
    print(baby1.swim()) # 첫째가 수영
    print(baby1.walk()) # 아빠가 걷기
    print(baby1.gene()) # XY
    ```
    

### 상속관련 함수와 메서드

- mro 메서드(Method Resolution Order)
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 >> 클래스 순으로 이름 공간을 탐색하는 과정
        - 상속관계에 있으면 인스턴스 >> 자식클래스 >> 부모클래스
    
    ```python
    print(Firstchild.mro())
    # [<class '__main__,FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class 'object'>]
    ```
    

---

## 3. 다형성

### 다형성(Polymorphism)이란?

- 여러 모양을 뜻하는 그리스어
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
- 즉,<mark> 서로 다른 클래스에 속해있는 객체들이 동일한 메세지에 대해 다른 방식으로 응답할 수 있음</mark>

### <mark>메서드 오버라이딩</mark>

- **상속받은 메스드를 재정의**
    - 클래스 상속 시, 부모의 크랠스에서 정의한 메서드를 자식 클래스에서 변경
    - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
    - 상속받은 클래스에서 같은 이름의 메서드로 덮어씀
    - **재정의 과정에서 부모 클래스의 메서드를 실행시키고 싶은 경우 super를 활용**
    
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
    
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
    
    # 자식 클래스 - Professor
    class Professor(Person):
        def talk(self): # 오버라이딩 # 부모클래스의 함수 실행 안됨.
            print(f'{self.name}일세.')
    
    # 자식 클래스 - student
    class Student(Person):
        def talk(self):
            super().talk() # 재정의 과정에서 부모클래스의 메서드를 실행시키고 싶은 경우
            print(f'저는 학생입니다.')
    
    p1 = Professor('김교수')
    p1.talk() # 김교수일세
    
    s1 = Student('이학생')
    s1.talk() 
    # 반갑습니다. 이학생입니다.
    # 저는 학생입니다.
    ```
    

- **VS 오버로딩**
- 오버로딩 : 같은 이름의 함수를 여러개 지정해서 상황에 맞게 각각 작동하도록 설정하는 것
    
    
- 파이썬에서 지원 안함
- 면접 단골 질문

---

## 4. 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
    - 예시 :  주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음

### 접근제어자 종류

1. Public Access Modifier
2. Protected Access Modifier
3. Private Access Modifier

### Public Member

- 언더바 없이 시작하는 메서드나 속성
- 어디서나 호출이 가능, 하위 클래스 override 허용
- 일반벅으로 작성되는 메서드와 속성의 대다수를 차지
    
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = 30
    
    # Person 클래스의 인스턴스인 p1은 이름(name)과 나이(age) 모두 접근 가능합니다.
    p1 = Person('김싸피', 30)
    print(p1.name) # 김싸피
    print(p1.age) # 30
    ```
    

### Protected Member ~~(?) 기존 방식이랑 차이점이 뭐지?~~

- 언더바 1개로 시작하는 메서드나 속성
    - <mark>그냥 내꺼라고 표현하는 것</mark>.
    - get_info같은 함수로 정보를 제공해줄 수 있지만 직접적으로 막 바꾸거나 조회하는 걸 방지
- 암묵적인 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스 override 허용
    
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def get_age(self):
            return self._age # Protected Member
    
    # 인스턴스를 만들고 get_age 메서드를 활용하여 호출
    # 실행시켜 확인해보세요.
    p1 = Person('김싸피', 30)
    print(p1.get_age()) # 30
    
    # _age에 직접 접근하여도 확인 가능
    # 파이썬에서는 암묵적으로 활용될 뿐입니다.
    print(p1._age) # 30
    ```
    

### Private Member

- 언더바 2개로 시작하는 메서드나 속성
- 본 클래스 내부에서만 사용이 가능
- 하위 클래스 상속 및 호출 불가능( 오류)
- 외부 호출 불가능(오류)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

# 인스턴스를 만들고 get_age메서드를 활용해서 호출 가능
p1 = Person('김싸피', 30)
print(p1.get_age()) # 30

# _age에 직접 접근이 불가능합니다.
print(p1.__age)
# AttributeError: 'Person' object has no attribute '__age'
```

### getter 메소드와 setter메서드

- 변수에 접근할 수 있는 메서드를 별도로 생성
- getter 메서드 : 변수의 값을 읽는 메서드
    - property 데코레이터 사용
- setter 메서드 : 변수의 값을 설정하는 성격의 메서드
    - @변수.setter 사용

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if new_age <= 19:
            raise ValueError('Too Young For here')
            return

        self._age = new_age

# 인스턴스를 만들어서 나이에 접근하면 정상적으로 출력됩니다.
# 실행시켜 확인해보세요.
p1 = Person(20)
print(p1.age) # 20
# p1 인스턴스의 나이를 다른 값으로 바꿔도 정상적으로 반영됩니다.
# 실행시켜 확인해보세요
p1.age = 33
print(p1.age) # 33

# setter 함수에는 '나이가 19세 이하면 안된다는' 조건문이 하나 걸려있습니다.
# 따라서 나이를 19세 이하인 값으로 변경하게 되면 오류가 발생합니다.
# 실행시켜 확인해보세요
p1.age = 19 # ValueError: Too Young For here
```

- setter 함수가 없어도, protected member는 setter 함수가 내부적으로 실행된다.
    
    
- 하지만 setter함수를 작성하면 조건문 등을 설정할 수 있다.