---

# 문자열

## 1. 문자의 표현

- 컴퓨터에 문자를 저장할 때 숫자로 저장함
- 영어가 대소문자 합쳐서 52이므로 6bit로 모두 표현 가능

### ASCII

- 문자 인코딩 표준
- 7bit  인코딩으로 128문자를 표현
  - 33개 : 출력 불가능한 제어 문자
  - 99개(32 ~ 126) : 공백을 비롯한 95개의 출력 가능한 문자들
- **확장 아스키**
  - 표준문자 이외의  악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문자를 128개 추가할 수 있게 하는 부호
  - 1byte 내의 8bit를 모두 사용함으로써 추가된 문자 표현
  - 서로 다른 프로그램이나 컴퓨터 사이에 교환 불가
    - 개발자가 여러가지 다양한 문자에 할당할 수 있도록 하기 때문에

### 유니코드

- 다국어 처리를 위한 표준
- UCS-(i)(Universal Character Set i) : 유니코드의 분류
  - 이를 인식하고 구분해서 인코딩이 요구됨

### 유니코드 인코딩(UTF : Unicode Transformation Format)

- UTF-8(in web)
  - Min : 8bit
  - Max : 32bit(1byte * 4)
- UTF-16(in windows, java)
  - Min : 16bit
  - Max : 32bit(2byte * 2)
- UFT-32(in unix)
  - Min : 32bit
  - Max : 32bit(4byte * 1)

### python 인코딩

- 2.x 버전 : ASCII → `#-*-coding: utf-8 -*-` (첫줄에 명시)
- 3.x 버전 - 유니코드 UFT-8 → 생략가능
- 다른 인코딩 방식으로 처리 시 첫줄에 작성하는 위 항목에 원하는 이코딩 방식 지정하면 됨

## 2. 문자열의 분류

### 2.1 fixed length

### 2.2 variable length

1. length controlled : java언어에서 문자열
2. delimited : c언어에서의 문자열

넘어가기{

### java에서 string 클래스에 대한 메모리 배치

- **java.lang.string 클래스**
  
  - 기본적인 객체 메타 데이터 : Flags, Locks
  - 이외 4가지 필드
    1. hash : hash값
    2. count : 문자열의 길이
    3. offset : 문자열 데이터의 시작점
    4. value : 실제 문자열 배열에 대한 참조

- **C언어에서 문자열 처리**
  
  - 문자열은 문자의 배열 형태로 구현된 응용 자료형
  
  - 끝에 널문자(’ \0’)를 넣어줘야 함
    
    }

### 파이썬에서의 문자열 처리

- char 타입 없음/ immutable
- 텍스트 데이터의 취급 방법이 통일되어 있음
- 문자열 기호
  - ‘’. “”, ‘’’ ‘’’
  - + : 연결
  - * : 반복
- 시퀀스 자료형으로 분류
  - 인덱싱, 슬라이싱 연산 가능
- 메소드
  - replace(), split(), isalpha(), find()

### C와 java의 string 처리의 차이점

- c는 아스키 코드로 저장
- java는 UTF-16, 2byte로 저장
- 파이썬은 UTF-8로 저장

## 3. 문자열 뒤집기

- s = s[::-1]

- s = ‘abcd’
  
  - s = list(s)
  - s.reverse()
  - ‘’.join(s)

- for문
  
  ```python
  s = 'Reverse this String'
  temp = ''
  for x in s[-1::-1]:
      temp += x
  
  s =temp
  ```
  
  ```python
  s = 'Reverse this String'
  temp = ''
  for x in s:
      temp = x + temp
  
  s = temp
  ```
  
  ```python
  s = 'Reverse this String'
  list_s = list(s)
  
  for idx in range(len(list_s)//2):
      list_s[idx], list_s[-1-idx] = list_s[-1-idx], list_s[idx]
  
  print(''.join(list_s))
  ```

## 4. <mark>문자열 비교</mark>

- C : strcmp() 함수 제공

- Java : equals() 메소드 제공
  
  - 문자열 비교에서 ==연산은 메모리 참조가 같은지를 묻는 것

- 파이썬 : ==연산자와 is 연산자를 제공
  
  - ==연산자는 내부적으로 특수 메서트 `__eq__()`를 호출
  
  - s1과 나머지 문자열을 ==, is로 비교한 결과를 확인하기
    
    ```python
    s1 = 'abc'
    s2 = 'abc'
    s3 = 'def'
    s4 = s1
    s5 = s1[:2] + 'c'
    
    print(s1 == s2) # True
    print(s1 == s3) # False
    print(s1 == s4) # True
    print(s1 == s5) # True
    
    print(s1 is s2) # True
    print(s1 is s3) # False
    print(s1 is s4) # True
    print(s1 is s5) # False
    ```

## 5. <mark>문자열 숫자를 정수로 변환</mark>

- 숫자와 문자변환 함수
  
  - int, float, str, repr

- 연습문제2_str() 함수를 구현하기
  
  ```python
  def itoa(num, strlist):
      # 음수인지 아닌지 판단
      neg = False # flag: 음수라면 True, 양수라면 False
  
      if num < 0:
          neg = True
          num = -num
  
      result = ''
      while num:
          num, remain = num//10, num % 10
          result = chr(ord('0') + remain)) + result
  
      if neg:
          return '-' + result
      else:
          return result
  
  res = itoa(1234)
  print(type(res), res)
  res = itoa(-1234)
  print(type(res), res)
  ```