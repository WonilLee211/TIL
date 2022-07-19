# 파이썬 기초_ 자료형_추가 학습

## 기초 문법(Syntax)

### 들여쓰기(indentation)

- 코드 블럭을 구분날 때 사용
- 4칸 공백 or 1탭
  - `**주의**` : 한 코드 안에서는 반드시 한 종류의 들여쓰기 사용하기
  - 원칙적으로 space 사용 권장
    
    

### 변수

- 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- **변수 x의 고유 메모리 주소를 확인**
  
  ```python
  >>> print(id(x))
  # 2542408651376
  ```

- **변수 할당 과정에서 에러**
  
  1. `cannot unpack non-iterable int object` `x , y = 1`
  2. `too many values to unpack (expected 2) x, y = 1, 2, 3`

- **식별자(indentifiers)**
  
  - 식별자의 이름은 영문 알파벳(대문자와 소문자), 언더스코어(_), 숫자로 구성
  - 첫 글자에 숫자가 올 수 없음
  - 길이에 제한이 없음
  - 대/소문자(case)를 구별
  - 아래의 키워드는 사용할 수 없음
  
  ```python
  False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```
  
  - **만일 변수로 사용했다면, `del 변수명` 명령하기!**
  
  ---
  
  

### 수치형

- 파이썬은 메모리를 동적으로 할당하기 때문에 변수에 아무리 큰 숫자를 넣어도 int 로 표기 가능

```python
>>> a = 2**10000
>>> print(type(a))
# <class 'int'>
```

- <mark>**오버플로우(overflow)**</mark>
  - 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어있음
  - 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 될 때, 기대했던 값이 출력되지 않는 현상
  - <mark>`해결책 :</mark>`**임의 정밀 산술(arbitrary-precision arithmetic)**.
  - 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는
  - 형태
- 파이썬이 얼만큼 큰 숫자까지 저장할 수 있을까?

```python
import sys
max_int = sys.maxsize
# sys.maxsize의 값은 2**63-1 64비트에서 부호비트를 뺀 63개의 최대치
print(max_int)
super_max = sys.maxsize**sys.maxsize
print(super_max)

#9223372036854775807
#85070591730234615847396907784232501249 # 최대 수 넘어서도 메모리 할당 가능
```

- **round()함수**
  
  - 소수에 대해서 짝수에서 5는 내림 / 홀수에서 5는 올림 `(부동소수점 문제에 의한 오류)`
  - round(값, 원하는 소수점자릿수)
  - 웬만하면 round()함수를 직접 구현하자

- 부동소수올림에러 해결 방법 3번째
  
  - `epsilon` 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
  
  ```python
  import sys
  abs(a - b) <= sys.float_info.epsilonla
  ```

---

### 문자열

- f-string
  
  - 형식을 지정할 수 있음(날짜)
  
  ```python
  import datetime
  today = datetime.datetime.now()
  print(today)
  
  print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
  # 오늘은 22년 07월 19일 Tuesday
  print(f'오늘은 {today:%Y}년 {today:%M}분 {today:%D}일 {today:%A}')
  # 오늘은 2022년 02분 07/19/22일 Tuesday
  ```
  
  - 연산과 출력 형식 지정
  
  ```python
  pi = 3.141592
  r = 2
  print(f'원주율은 {pi:.3}, 원의 넓이는 {r**2*pi}')
  
  # 원주율은 3.14, 원의 넓이는 12.566368
  ```

### 딕셔너리

- 딕셔너리에서 중복된 key는 존재할 수 없다.

```python
dict_a = {1: 1, 2: 2, 3: 3, 1: 4}
print(dict_a)

# {1: 4, 2: 2, 3: 3}
```

- phone_book.items()

```python
print(phone_book.items())
# dict_items([('서울', '02'), ('구미', '054'), ('대전', '042'), ('광주', '061'), ('부울경', '051')])
# key:value 조합을 **튜플** 형태로 각각 반환
```

---



# 형변환(Type Conversion, Typecasting)

## 1. 암시적 형변환

- bool
- Numeric Type(int, float, complex)

```python
a = True + 10
print(a, type(a))
# 11 <class 'int'>
```

## 2. 명시적 형변환(Explicit Typecasting)

- 내장함수 사용하기

## 비교연산자

- is : 타입이 같은지 확인
- == : 값이 같은지

## <mark>**단축평가(중요!)</mark>**

```python
>>> 'a' and 'b'
# 'b'
>>> 'a' or 'b'
# 'a'

>>> vowels = 'aeiou'

>>> 'a' and 'b' in vowels
# False

>>> ('a' and 'b') in vowels
# False

>>> 'b' and 'a' in vowels
# False 라고 생각했는데 True임..

>>> ('b' and 'a') in vowels
# True

>>> 'a' or 'b' in vowels
# 'a'

>>> 'b' or 'a' in vowels
# 'b'

>>> ('a' or 'b') in vowels
# True

>>> ('b' or 'a') in vowels
# False
```

## 인덱싱/슬라이싱

- `[]` 를 통한 값을 접근하고, [:]을 통해 슬라이싱
- 리스트, 튜플, range, 문자열 접근 가능

```python
>>> range(3)[2]
# 2
```

## <mark>연산자 우선순위</mark>

- 0. `()` 을 통한 그룹핑
- 1. slicing
- 2. indexing
- 3. 제곱연산자 `**` (`-2**2 # -4`)
- 4. 단항연산자 `+` , `-` ( 음수, 양수 부호)
- 5. 산술연산자 `*`, `
- 6. 비교연산자 `in`, `is`
- 7. `not`
- 8. `and`
- 9. `or`

## 식별자 ==변수

## <mark> 표현식(Expression)과 문장(statement)의 구분(중요!)</mark>

### 표현식

- 새로운 데이터 값을 생성하는 코드 조각
- 코드 실행 후 값으로 나오는 경우( 출력이 되는 경우)
- 출력이 안되면, 표현식이라 할 수 없음

```python
>>> a = 10    # 문장
>>> a > 10    # 문장이자, 표현식
# False

>>> 5 * 21 - 4    # 표현식
```

### 문장

- 특정한 작업을 수행하는 코드 전체
- 실행가능하면 모두 문장이라고 할 수 있음
