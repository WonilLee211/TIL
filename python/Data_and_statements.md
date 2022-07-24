# 목차

1. 학습목표
2. 수업OT
3. 프로그래밍 학습 마인드셋
4. 프로그래밍이란?
5. 파이썬이란?
6. 파이썬 기초 문법
   1. 코드작성법
   2. 변수
   3. 연산자
   4. 자료형
   5. 시퀀스 컨테이너
      1. 리스트
      2. 튜플
      3. range
      4. 슬라이싱 연산자
   6. 비시퀀스 컨테이너
      1. 셋
      2. 딕셔너리
      3. 형 변환
7. 파이썬 프로그램 구성 단위
8. 프로그램 설치
   1. marktext 
   2. jupyter
   3. 개발자용 폰트

---

# 학습목표

- 효율적으로 프로그래밍하는 방법
- 파이썬을 학습해야 하는 이유
1. 수업 OT
2. 프로그래밍이란?
3. 파이썬과 파이썬 개발환경
4. 파이썬 기초 문법
5. 자료형
6. 컨테이너

---

# 수업 OT

1. 개념구조화하기
2. 기본기 탄탄하게 쌓기
3. 동료학습

---

# 프로그래밍 학습 마인드 셋

## 1. 개념 구조화하기

- **구조화** : 해당 개념과 하위 개념들을 잘 묶어서 머리 속에 저장하는 것

- **구조**
  
  1. 개념 정의
  2. 개념의 포함 관계
  3. 두 개념의 차이점
  
  `※기술면접에도 활용됨 !`

## 2. 기본기 탄탄하게 쌓기

- 코드를 많이 쳐보기
- 문법 문제 풀기

## 3. 동료학습

- 배운 개념 설명하기
- 코드의 에러 함께 해결하기
- 모르는 내용을 서로 질문/대답하면서 지식의 빈틈 채우기
- 커뮤니케이션 스킬 증진

---

# 프로그래밍이란?

1. 프로그램ㅣㅇ의 정의
2. 프로그래밍의 원리
   1. 언어?
   2. 소스코드?
   3. 번역기?

## 1. 프로그래밍의 정의

- 프로그램을 만드는 행위
  - 프로그램 : 특정 작업을 수행하는 일련의 명령어들의 모음
- **컴퓨터에게 일을 시키기 위해서 프로그램을 만드는 행위**

## 2. 프로그래밍 언어란?

### - 언어란

1. 자신을 생각을 나타내고 전달하기 위해 사용하는 체계

2. 문법적으로 맞고 언어 공동체 내에서 이해될 수 있는 말의 집합
- 컴퓨터는 기계어로 소통 : 0과 1로 모든 것을 표현(2진법)

### 특징

- 사람이 이해할 수 있는 문자로 구분
- 기본적인 규칙과 문법이 존재함

### 소스코드

- 프로그래밍 언어로 작성된 프로그램

### 번역기(interpreter or compiler)

- 소스코드를 컴퓨터가 이해할 수 있는 기계어로 번역
- 파이썬은 interpreter 사용

---

# 파이썬이란?

1. 배워야하는이유
2. 특징
3. 개발환경

## 1. 파이썬을 배워야 하는 이유

1. 일고리즘 코딩 테스트에 유리
   1. 변칙적인 유형에 대응하기 쉬움
2. 구현 코딩 테스트에 유리
   1. 유용한 라이브러리가 많고 최소한만 사용해서 프로그램을 개발하는데 유리함
   2. 실행시간이 매우 중요한 문제 유형이 아니면 유리함.
3. AI개발, 데이터 분석, 웹 프로그래밍, 업무자동화 등 파이썬 활용 분야 증가
4. EASIER TO LEARN THAN OTHERS

## 2. 파이썬 특징

### 1. 인터프리터 언어

### 2. 객체 지향 프로그래밍

- 현대 프로그래밍의 기본적인 설게 방법론으로 자리잡은 방식
- 모든 것이 객체로 구현되어 있음

## 3. 파이썬 개발환경

### 종류

1. IDE
2. Jupyter
3. IDLE(intergrated Development and Learning Evironment)

### 1. IDE (intergrated development environment)

- 통합 개발 환경의 약자
- 다양하고 강력한 기능들을 모아둔 프로그램
- 보통 개발을 IDE로 진행
- VS코드나 Pycharm

### 2. Jupyter Notebook

- 문법 연습을 위한 최적의 도구
- 셀 단위의 실행이 가능한 점이 특징

### 3. 목적에 따른 개발환경

1. 문법학습 : 쥬피터

2. 웹 : VS code
   
   1. HTML/CSS/Django, Javascript, Vue 등 모두 개발하기 편한 환경

3. 알고리즘 : Pycharm & VS code
- ※ **vscode 단축키**
  
  alt + 여러 줄 커서 클릭 ; 여러줄에 동시에 타이핑 가능
  
  alt + ctrl + 화살표 : 멀티 커서 넓힘(동시 타이핑 가능)
  
  alt + 화살표 : 코드 움직임
  
  ctrl + 단어 선택 : 동일한 단어 모두 편집 가능
  
  ctrl + D : 선택되어있는 문자열(또는 커서 주변의 단어)를 선택해서 추가
  
  alt + shift + 화살표 : 줄 복사

---

# 기초 문법

## 코드 작성법

### 코드 스타일 가이드

- 코드를 어떻게 작성할지에 대한 가이드 라인
  - PEP8에 따라서 공부하기
  - [PEP 8 – Style Guide for Python Code | peps.python.org](https://python.org/dev/peps/pep-0008/)

### PEP8

- max line length : 79자
- names to avoid : 소문자 L, 대문자 O, 대문자 i
- 띄어쓰기 규칙, 따옴표 종류 통일
- 맞춤법 지키기

### 들여쓰기

- 문장을 구분할 때

### 주석

- 코드에 대한 설명
- 복잡한 코드를 쉽게 이해할 수 있도록 도움(소통에 용이)
- 한줄 주석
  - `print("SSAFY KIM") # 주석`
- 여러줄 주석
  - ‘’’ ‘’’ / “”” “””

## 변수

- 데이터를 받는 상자
- 복잡한 값을 쉽게 사용할 수 있음**(추상화)**
- 동일한 변수에 다른 데이터를 언제들 할당할 수 있기 때문에 변수라고 불림

### 1. 변수 할당

```python
americano_price = cookie_price = 2000
```

### 2. 변수값 바꿔서 저장

```python
x ,y = 10, 20

tmp = x
x = y
y = tmp

print(x, y) # 20, 10
```

- pythonic!

```python
x, y = y, x

print(x, y) # 20, 10
```

### 3. 식별자

- 변수이름 규칙
  
  - 영문 알파벳, 언더스코어( _ ), 숫자로 구성
  - 첫 글자에 숫자가 올 수 없음
  - 길이에 제한이 없고 대소문자로 구별
  - 다음 키워드는 제한 예약어로, 사용 안됨
  
  ```python
  import keyword
  print(keyword.kwlist)
  
  '''
  ['False', 'None', 'True', '__peg_parser__', 'and', 
  'as', 'assert', 'async', 'await', 'break', 'class',
   'continue', 'def', 'del', 'elif', 'else', 'except',
   'finally', 'for', 'from', 'global', 'if', 'import',
   'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
   'raise', 'return', 'try', 'while', 'with', 'yield']
  '''
  ```
  
  - 내장함수나 모듈 등의 이름도 사용하면 안됨

### 4. 연산자

- , - , * , / , // , **

### 5. 자료형 분류

1. Boolean : 참거짓. True, False
2. Numeric
   1. int : 정수
   2. float : 실수
   3. complex : 복소수
3. String : 문자열
4. None

### 수치형

1. 진수 표현
   
   1. 여러 진수 표현 가능
      
      1. 2진수(binary) : 0b
      2. 8진수 (octal) : 0o
      3. 16진수 (hexadecimal) : 0x
      
      ```python
      print(0b10) # 2
      print(0o30) # 24
      print(0x10) # 16
      ```

2. **실수 연산 시 주의할 점** - `부동 소수점, floating point round error`
   
   1. 컴퓨터는 2진수, 사람은 10진수를 사용
   2. 10진수 0.1을 2이진수로 표현하면 0.0001100.. 무한으로 표현 >> 오차 발생 >> 근사값만 표현함
   
   **`해결책`**
   
   매우 작은 수보다 작은지 확인하거나 math 모듈 사용
   
   ```python
   a = 3.2 - 3.1 # 0.100000000000000000000009
   b = 1,2 - 1.1 # 0.099999999999999999999987
   
   # 1. 임의의 작은 수 활용
   print(abs(a-b) < 1e-10) # True
   
   # 2. python 3.5 이상
   import math
   print(math.isclose(a,b)) # True
   ```

### 문자열 자료형

- 모두 str 타입
- ‘’ or “”
- 중첩 따옴표

```python
print("문자열 안에 '작은 따옴표'를 사용하려면 큰 따옴표로 묶기")
print('문자열 안에 "큰 따옴표"를 사용하려면 작은 따옴표로 묶기')
```

- 삼중 따옴표

```python
print('''문자열 안에 '작은 따옴표'나 
"큰 따옴표"를 사용할 수 있고
 여러 줄을 사용할 때도 편리하다''')
```

- escape sequence
  
  - \n : 줄바꿈
  - \t : 탭
  - \r : 캐리지 리턴
  - \0 : 널(Null)
  - \\ : \
  - \’ : 단일 인용 부호
  - \” : 이중 인용 부호
  
  ```python
  print('철수 \\'안녕\\' ') # 철수 '안녕'
  print('이 다음은 엔터. \\n 그리고 탭\\t탭')
  # 이 다음은 엔터.
  #    그리고 탭    탭
  ```

- 문자열 연산
  
  - 덧셈, 곱셈

- String interpolation(문자열과 변수를 활용하려 만드는 법)
  
  - str.format()
  
  ```python
  name = 'kim'
  score = 4.5
  
  print('Hello, {}! 성적은 {}'.format(name, score))
  # Hello, Kim! 성적은 4.5
  ```
  
  - **f-string : python 3.6+**
  
  ```python
  name = 'kim'
  score = 4.5
  print(f'Hello, {name}! 성적은 {score}')
  # Hello, Kim! 성적은 4.5
  
  import datetime
  today = datetime.datetime.now()
  print(today) # 2022-07-08 16:04:15.200411
  
  print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
  # 오늘은 22년 07월 08일
  
  pi = 3.141592
  print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
  # 원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368
  ```

### None

- 파이썬 자료형 중 하나
- 값이 없음을 표현
- 반환 값이 없는 함수에도 사용

### 불린형

- 참/거짓 표현하는 자료형

- 값 : True, False

- 비교/논리 연산에서 활용
  
  ### 비교 연산자
  
  - < , <= , > , >= , == , !=
  - is : 객체 아이덴티티(OOP)
  - is not : 객체 아이덴티티가 아닌 경우
  
  ### 논리 연산자
  
  - and , or , not
  
  ### 주의할 점
  
  - Falsy : False는 아니지만 False로 취급되는 다양한 값
    
    - 0, 0.0 , () , [] , {} , None , “”(빈 문자열)
  
  - 논리 연산자도 우선순위가 존재
    
    - not > and > or 순으로 우선순위가 높음
    
    ```python
    print(not True) # False
    print(not 0) # True
    print(not 'hi') # False
    print(not True and False or not False) 
    # True. (False and False) or True로 해석됨.
    #위와 같은
    print(((not True) and False) or (not False)) # True
    ```

- 논리 연산자의 단축 평가
  
  - 결과가 확실한 경우 두번째 값 확인하지 않고 첫번째 값 반환
  
  ```python
  print(3 and 5) # 5
  print(3 and 0) # 0
  print(0 and 3) # 0
  print(0 and 0) # 0
  
  print(5 or 3) # 5
  print(3 or 0) # 3
  print(0 or 3) # 3
  print(0 or 0) # 0
  ```

## 컨테이너

- 여러 개의 값을 담을 수 있는 객체

- ex> list

- 종류 :
  
  1. 순서(인덱스)가 있는 데이터(시퀀스 컨테이너)
  
  2. 가변형 : 리스트 [ ]
  
  3. 불변형 : 튜플 ( ) / 레인지 range(int)
  
  4. 순서가 없는 데이터(비시퀀스 컨테이너)
     
     1. 가변형 : 세트{ } / 딕셔너리 {key:value}
  
  ### 1. 리스트
  
  - 리스튼 여러 개의 값을 **순서가 있는 구조로 저장**하고 싶을 때 사용
  - 파이썬에서는 어떤 자료형도 저장할 수 있음
  - 생성 이후 내용 변경이 가능
  - 생성방법
    1. [ ]
    2. list()
  
  ### 2. 튜플
  
  - 리스트와의 차이점 : 불변 자료형. 담은 후 변경 불가
  
  - 인덱스로 접근 가능
  
  - 생성 방법
    
    1. ()
    2. tuple()
  
  - `주의사항`
    
    - 단일항목인 경우 : 값 뒤에 쉼표를 붙여야 함.
    - 복수항목인 경우 : 마지막 항목에 붙은 쉼표는 없어도 되지만 **넣는 것을 권장**
    
    ```python
    tuple_a = (1,)
    print(tuple_a) # (1,)
    print(type(tuple_a)) # <class 'tuple'>
    
    tuple_b = (1, 2, 3,)
    print(tuple_b) # (1, 2, 3)
    print(type(tuple_b)) # (1, 2, 3)
    print(type(tuple_b) # <class 'tuple'>
    
    b = 1, 2, 3
    print(b) # (1, 2, 3)
    print(type(b)) # <class 'tuple')
    ```
  
  - 튜플 대입
    
    - 우변의 여러 값들을 좌변의 여러 변수에 한 번에 할당하는 과정
  
  ### 3. Range
  
  - 숫자의 시퀀스를 나타내기 위해 사용
  
  - 종류
    
    1. 기본형 : range(n)
    2. 범위 지정 : range(n, m)
    3. 범위 및 스텝 지정 : range(n, m, s)
       1. n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스
    
    ```python
    # 0부터 특정 숫자까지
    print(list(range(3))) # [0, 1, 2]
    
    # 숫자의 범위
    print(list(range(1, 5))) # [1, 2, 3, 4]
    
    # step 활용
    print(list(range(1, 5, 2))) # [1, 3, 5]
    
    # 역순
    print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2]
    
    print(list(range(6, 1, -2))) # [6, 4, 2]
    
    print(list(range(6, 1, 1))) # []
    ```

### ※ 슬라이싱 연산자

- 시퀀스를 특정 단위로 슬라이싱
- 인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라내기

```python
# 리스트([1:4]에서 1은 포함 4는 미포함
print([1,2,3,5][1:4]) # [2, 3, 5]

print([1, 2, 3, 5][0:4:2]) # [1, 3]

# 튜플
print((1, 2, 3)[:2]) # (1, 2)
print((1, 2, 3, 5)[0:4:2]) # (1, 3)

# range
print(range(10)[5:8]) # range(5,8)
print(range(10)[1:5:3]) # range(1, 5, 3)

# 문자열
print('abcd'[2:4]) # cd
print('abcdefg'[1:3:2]) # b

s = 'abcdefghi'
s[2:5] # 'cde'
s[2:5:2] # 'ce'
s[5:2:-1] # 'fed'
s[:3] # 'abc'
s[5:] # 'fghi'
s[::-1] # 'ihgfedcba'
```

### 4. set

- 중복되는 요소가 없이, 순서에 상관없는 데이터의 묶음

- 중복되는 요소는 하나만 저장

- 인덱스 접근 불가

- 수학에서의 집합을 표현한 컨테이너
  
  - 집합 연산 가능
  - 중복된 값 없음

- 가변 자료형(삽입, 변경, 삭제 가능)

- 생성방법
  
  ```python
  # 중복 값 제거
  print({1, 2, 3, 1, 2}) # {1, 2, 3}
  print(type({1, 2, 3})) # <class 'set'>
  
   # 빈 중괄호는 Dictionary
  blank = {}
  print(type(blank)) # <class 'dict'>
  blank_set = set()
  print(type(blank_set)) # <class 'set'>
  
  # Set은 순서가 없어 인덱스 접근 등 특정 값에 접근할 수 없음
  print({1, 2, 3}[0]) # TypeError: 'set' object is not subscriptable
  ```

- 연산자
  
  ```python
  A_set = {1, 2, 3, 4}
  B_set = {1, 2, 3, "Hello", (1, 2, 3)}
  
  # 합집합
  print(A_set | B_set) # {1, 2, 3, 4, (1, 2, 3), "Hello'}
  # 교집합
  print(A_set & B_set) # {1, 2, 3}
  # 차집합
  print(B_set - A_set) # {(1, 2, 3), "Hello"}
  # 대칭 차집합 : 합집합에서 교집합 뺀 것
  print(A_set ^ B_set) # {"Hello", 4, (1, 2, 3)}
  ```

### 5. 딕셔너리

- key-value 쌍으로 이뤄진 자료형(3.7부터는 ordered, 이하 버전은 unordered)

- key를 통해 value에 접근

- key
  
  - 변경불가능한 데이터만 가능
    
    ex) string, integer, float, boolean, `tuple`, range

- value
  
  - 모든 형태 가능

- 생성방법
  
  1. {}
  2. dict{}

### 형 변환(Typecasting)

- 파이썬에서 테이터 형태를 서로 변환할 수 있음
1. **암시적 형 변환(implicit)**
   
   - 사용자가 의도하지 않고 파이썬 내부적으로 자료형을 변환하는 경우
   
   - 종류
     
     - bool
     - Numeric type (int, float)
     
     ```python
     print(True + 1) # 4
     print(3 + 5.0) # 8.0
     ```

2. **명시적 형 변환(explicit)**
   
   - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
   
   - 종류
     
     - int
     - float
     - str
     
     ```python
     # 문자열은 암시적 타입 변환이 되지 않음
     print('3' + 4) # TypeError: can only concatenate str (not "int") to str
     
     # 명시적 타입 변환이 필요함
     print(int('3') + 4) # 7
     
     # 정수 형식이 아닌 경우 타입 변환할 수 없음
     print(int('3.5') +5) # ValueError: invalid literal for int() with base 10: '3.5'
     
     print('3.5' + 3.5) # TypeError: can only concatenate str (not 'float') to str
     
     # 정수 형식인 경우에도 float으로 타입 변환
     print(float('3')) # 3.0
     
     # float형식이 아닌 경우 타입 변환을 할 수 없음
     print(float('3/4') + 5.3) # ValueError: could not convert string to float: '3/4'
     
     # str으로 변화는 거의 다 된다
     print(str(1)) # '1'
     print(str(1.0)) # '1.0'
     print(str([1, 2, 3])) # '[1, 2 ,3]'
     print(str((1, 2, 3))) # '(1, 2, 3)'
     print(str({1, 2, 3})) # '{1, 2, 3}'
     ```

3. **컨테이너 형 변환**
   
   - 컨테이너 간의 형변환
   - 목록 [string, list, tuple, range, set, dictionary]
     - range로의 변환은 불가
     - dictionary로의 변환은 불가
     - 딕셔너리는 key만 list, tuple, set으로 형 변환 가능

---

# 파이썬 프로그램 구성 단위

## 파이썬 구성단위

- 식별자
  - 변수 함수 클래스 등
- 리터럴
  - 읽혀지는 대로 쓰여있는 값 그 자체
- 표현식
  - 새로운 데이터 값을 생성하거나 계산하는 코드 조각
- 문장
  - 특정한 작업을 수행하는 코드 전체
  - 파이썬이 실행 가능한 최소한의 코드 단위
  - 표현식이 값을 생성하는 일부분이고, 문장은 특정 작업을 수행하는 코드 전체
- 패키지
  - 프로그램과 모듈 묶음
- 라이브러리
  - 패키지 묶음

---

# 설치

### 마크 택스트 설치

- marktext 검색 - github - download
- 설정
  - 이미지 - assets folder 켜기
  - 폴더 이름 : `${filename}_assets`

**이미지넣을 때 주의**

- 문서를 저장하지 않고 이미지를 붙여넣으면, 파일이 기본 폴더로 저장돼서 따라오지 않음.
- `결론 : **파일 만들고 저장 먼저 하기**`

### 개발자용 폰트 설치

- 네이버 D2coding
- 깃헙에서 D2coding-ver1.3.2-20180524.zip설치
- 각 폴더에 폰트들 오른쪽 클릭
- 모든 사용자용으로 설치 클릭

### vs코드 폰트 적용

- 설정 ctrl + ,
- font 검색
- font family에 `D2coding, Consolas, 'Courier New', monospace`

### jupyter 설치

- notion 참고

### 크롬 폰트 설정

- 노션 참고
