# 자료 구조

# 목차

## 순서가 있는 데이터 구조

- 문자열(String)
- 리스트(List)
- 튜플(Tuple)

## 순서가 없는 데이터 구조

- 셋(Set)
- 딕셔너리(Dictionary)

## 얕은 복사와 깊은 복사

---

## 데이터 구조 활용

### 1. 메서드

- 클래스 내부에서 정의한 함수, 사실상 함수 동일
- 데이터 구조를 활용하는데 사용
- `데이터구조.메서드()` 형태로 활용

### 2. 파이썬 공식 문서의 표기법(베커스-나우르 표기법)

- 컴퓨터 언어에서 언어의 문법을 수학적인 수식으로 나타낼 때 사용하는 언어도구
- 프로그래밍 언어의 구문을 기술하는 데 매우 자연스러운 표기법
- python 구문이 아니며, 베커스-나우르 표기법
- ex) `str.replace(old, new[, count])`
    - old, new는 필수/ [,count]는 선택적 인자를 의미함

---

# 순서가 있는 데이터 구조

## 1. 문자열(String Type)

- 문자들의 나열(sequence of Characters)
    - 모든 문자는 변경불가능한 immutable string type
- ‘’나 “”를 활용하여 표기
- PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함.

### 1.1 문자열 조회 및 탐색 및 검증 메서드

|문법|설명|
|:---:|:---|
|`s.find(x)`| x의 첫 번째 위치를 번환, 없으면 -1 반환| 
|`s.index(x)`| x의 첫 번째 위치를 반환. 없으면, 오류 발생|
|`s.isalpha()`|알파벳 문자 여부 * 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)|
|`s.isupper()`|대문자 여부|
|`s.islower()`|소문자 여부|
|`s.istitle()`|타이틀 형식 여부(처음 알파벳이 대문자니?) |

### 1.2 문자열 조회 및 탐색

1. `.find(x)` : x의 첫 번째 위치를 반환. 없으면, -1 반환
    - <mark> vs `s.index(x)`와의 차이점 숙지하기 </mark>

```python
print('apple'.find('p')) # 1
print('apple'.find('k')) # -1
```

2. `.index(x)` : x의 첫 번째 위치를 반환. 없으면, 에러발생

```python
print('apple'.index('p') # 1
print('apple'.index('k') # ValueError : substring not found
```

### 1.3 문자열 관련 검증 메서드

```python
print('abc'.isalpha()) # True
print('ㄱㄴㄷ'.isalpha()) # True
print('Ab'.isupper()) # False
print('ab'.islower()) # True
print('Title Title!'.istitle()) # True
```

- isdecimal() : 진짜 숫자야?10진수
- isdigit() :  수야?
- isnumeric() : 숫자로 볼 수도 있지 않나?
    - 명백한 문자열은 안됨…..
    - 이런게 있다 ~ 정도만 알기

### 1.4 문자열 변경 메서드

- `s.replace(old, new[ ,count])` : 바꿀 대상을 새로운 글자로 바꿔서 반환
    - count를 지정하면 해당 개수만큼 시행
    
    ```python
    print('coone'.replace('o', 'a')) # caane
    print('wooooowoo'.replace('o', '!', 2)) # w!!ooowoo
    ```
    
- `s.strip([chars])`: 공백이나 특정 문자를 제거
    - 작동방식 : char의 문자가 s의 양옆에 있다면 제거, 없다면 break
    ```python
    print('   와우!\n'.strip()) # 와우!
    print('   와우!\n'.lstrip()) # 와우!
    print('   와우!   \n'.rstrip()) # '   와우!'
    print('안녕하세요????'.rstrip('?')) # 안녕하세요
    ```
    
- `s.split(sep=None, Maxsplit=-1)` : 공백이나 특정 문자를 기준을 분리
    - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주(선행/후행 공백은 빈 문자열에 포함 안함
    - maxsplit(split 횟수)에 -1인 경우 제한이 없음

```python
print('a,b,c'.split('_')) # ['a,b,c']
print('a b c'.split()) # ['a', 'b', 'c']
```

- `‘separator’.join([iterable])` : 구분자로 iterable 합침
    - iterable에 문자열이 아닌 값이 있으면 `typeError`
    - `+`문자열 합치는 거보다 빠르다!!!!
    
    ```python
    print('!'.join('wonil')) # w!o!n!i!l
    print(' '.join(['3', '5'])) # '3 5'
    ```
    
- `s.capitalize()` : 가장 첫 번째 글자를 댐분자로 변경
- `s.title()` : 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환
- `s.upper()` : 모두 대문자로 변경
- `s.lower()` : 모두 소문자로 변경
- `s.swapcase()` : 대 소문자 서로 변경

```python
msg = 'hI! Everyone, I\'m 원일'

print(msg.capitalize()) # Hi! everyone, i'm 원일
print(msg.title()) # Hi! Everyone, I'M 원일
print(msg.upper()) # HI! EVERYONE, I'M 원일
print(msg.lower()) # 'hI! everyone, i'm 원일'
print(msg.swapcase()) # 'hi! eVERYONE,i'M 원일'
```

---

## 2. 리스트 List

- 순서가 있는 구조로 정하고 싶을 때 사용

### 2.1 리스트 생성과 접근

- 대괄호, [] 혹은 list()를 통해 생성
- 파이썬에서는 어떤 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음
- mutable 자료형
- 값에 대한 접근 list[i]
    
    ```python
    list_a = []
    list_b = [1, 2, 3]
    list_c = ['life', 'is', 'too', 'short']
    list_d = [1, 2, 3, 'Python', ['리스트', '안에', '리스트']]
    ```
    

### <mark> 2.2 리스트 메서드 </mark>

<h4> <mark> 값 추가 및 삭제 </mark> </h4>

1. `L.append(x)` : 리스트 마지막에 항목 x를 추가
2. ` L.insert(i, x)` : 리스트 인덱스 i에 항목 x를 삽입
    
    ```python
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.inset(len(cafe),'end')
    print(cafe) # ['starbucks','tomntoms','hollys', 'end']
    
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.inset(1000,'end') # i가 리스트 길이보다 크면 맨 뒤
    print(cafe) # ['starbucks','tomntoms','hollys', 'end']
    ```
    
3. `L.extend(m)` : 순회형 m의 모든 항목들을 리스트 끝에 추가( +=과 같은 기능)
    - append()와 차이점 파악하기
    ```python
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.extend(['coffee'])
    print(cafe) # ['starbucks','tomntoms','hollys', 'coffee']
    
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe += ['coffee']
    print(cafe) # ['starbucks','tomntoms','hollys', 'coffee']
    
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.extend('coffee')
    print(cafe) # ['starbucks','tomntoms','hollys', 'c', 'o', 'f', 'f', 'e', 'e']
    ```
    
4. ` L.remove(x)` : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거
    -  항목이 존재하지 않는 경우, valueError
    

    ```python
    numbers = [1, 2, 3, 'hi']
    numbers.remove('Hi')
    print(numbers) # [1, 2, 3]
    
    numbers.remove('hi')
    # ValueError : list.remove(x) : x not in list
    ```
    
5. ` L.pop(i)` : 리스트의 인덱스 i에 있는 항목을 반환 후 제거
    1. i가 없으면 마지막 항목을 삭제하고 반환
    
    ```python
    numbers = ['hi', 1, 2, 3]
    numbers.pop()
    print(numbers) # ['hi', 1, 2]
    
    numbers = ['hi', 1, 2, 3]
    numbers.pop(0)
    print(numbers) # [1, 2, 3]
    ```
    
6. `L.clear()` : 모든 항목을 삭제함
    
    ```python
    numbers = [1, 2, 3, 'hi']
    numbers.clear()
    print(numbers) # []
    ```
    

<h4> <mark> 탐색 및 정렬 </mark> </h4>

1. `L.index(x, start, end)` : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
    
    ```python
    numbers = [1, 2, 3, 4]
    print(numbers.index(3)) # 2
    print(numbers.index(100)) # ValueError: 100 is not in list(없는 경우)
    ```
    
2. `L.reverse()` : 리스트를 거꾸로 정렬
    
    ```python
    numbers = [3, 2, 5, 1]
    result = numbers.reverse()
    print(numbers, result) # [1, 5, 2, 3] None
    ```
    
3. `L.sort()` : 원본 리스트를 정렬( 매개변수 이용 가능)
    1. None을 반환
    2. VS sorted(list) : 리스트를 정렬해서 새로운 리스트 반환
    
    ```python
    numbers = [3, 2, 5, 1]
    result = numbers.sort()
    print(numbers, result) # [1, 2, 3, 5] None 원본 변경
    
    numbers = [3, 2, 5, 1]
    result = sorted(numbers)
    print(numbers, result) # [3, 2, 5, 1] [1, 2, 3, 5]
    ```
    
4. <mark>`L.count(x)` : 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환</mark>
    
    ```python
    numbers = [1, 2, 3, 1, 1]
    print(numbers.count(1)) # 3
    print(numbers.index(100)) # 0
    ```
    ```python
    def sum_of_repeat_number(numbers):
        numbersset = set(numbers)

        total = 0
        for num in numberset:
            if numbers.count(num) == 1:
                total += num
        
        return total
    ```

## 튜플

- 여러개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
- 리스트와의 차이점 : 담고 있는 값 변경이 불가(불변 자료형)
- 항상 소괄호 형태 사용

### 튜플 관련 메서드

- immutable 이기에 값에 영향을 주지 않는 메서드만 지원
- 리스트 메서드 중 항목을 변경하는 메서드 외에 대부분 동일
- <mark> 확장연산자</mark>

```python
#확장연산자 : 값을 병합해서 재할당(같은 자료형)
day_name = ('월', '화', '수', '목', '금')
day_name += False, True
print(day_name)
# ('월', '화', '수', '목', '금', False, True)
```

---

# 비시퀀스형 데이터구조

## 1. 셋(Set)

- 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
    - 데이터의 중복을 허용하지 않기 때문에 중복 요소는 하나만 저장
    - 순서가 없기 때문에 인덱스를 이용한 접근 불가
- 수학에서의 집합을 표현한 컨테이너
    - 여집합을 제외한 집합 연산 가능
    - 중복된 값이 존재하지 않음
    - mutable 자료형
    
    ### 셋 메서드
    
    <h4> <mark> 추가 및 변경 </mark> </h4>
    
    1. `s.copy()` : 셋의 얕은 복사본을 반환
    2. `s.add(x)` : 항목 x가 셋 s에 없다면 추가
        
        ```python
        a = {'사과', '바나나', '수박'}
        a.add('딸기')
        print(a) # a = {'사과', '딸기', '바나나', '수박'}
        ```
        
    3. `s.update(#others)` : 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가
        
        ```python
        a = {'사과', '바나나', '수박'}
        a.update(['딸기', '바나나', '참외'])
        print(a) # {'참외', '사과', '딸기', '바나나', '수박'}
        ```
        
    
    <h4> <mark>요소 삭제 </mark> </h4>
    
    1. `s.remove(x)` : 항목 s를 삭제
        1. 항목이 존재하지 않을 경우, KeyError
        
        ```python
        a = {'사과', '바나나', '수박'}
        a.remove('사과')
        print(a) # {'바나나', '수박'}
        a.remove('애플')
        print(a) # KeyError: '애플'
        ```
        
    2. `s.pop()` : 셋 s에서 **랜덤**하게 항목을 반환하고, 해당 항목을 제거
        1. set이 비어 있을 경우, KeyError
        
        ```python
        a = {'사과', '바나나', '수박'}
        a.pop('사과')
        print(a) # {'사과', '수박'}
        
        ```
        
    3. `s.discard(x)` : 항목 x가 셋 s에 있는 경우, 항목 ,x를 셋 s에서 삭제
        1. 셋에서 삭제하고 **없어도 에러가 발생하지 않음**
        
        ```python
        a = {'사과', '바나나', '수박'}
        a.discard('사과')
        print(a) # {'바나나', '수박'}
        a.discard('애플')
        print(a) # {'바나나', '수박'}
        ```
        
    4. `s.clear()` : 모든 항목을 제거
    
    <h4> <mark>상하위 관계 판별 </mark> </h4>
    
    1. `s.isdisjoint(t)` : 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우 True
    2. `s.issubset(t)` : 셋 s가 셋 t의 하위 셋인 경우 True
    3. `s.issuperset(t)`: 셋 s가 셋 t의 상위 셋인 경우 True
        
        ```python
        a = {'사과', '바나나', '수박'}
        b = {'포도', '망고'}
        c = {'사과', '포도', '망고', '수박', '바나나'}
        
        print(a.isdisjoint(b)) # 서로소인가? True
        print(a.isdisjoint(c)) # 서로소인가? False
        print(a.issubset(c)) # 서로소인가? True
        print(a.isuperset(c)) # 서로소인가? False
        print(c.isuperset(a)) # 서로소인가? True
        ```
        
    

## 2. 딕셔너리(Dictionary)

- 키- 값 쌍으로 이루어진 자료형(3.7부터는 ordered)
- 딕셔너리의 키
    - 변경불가능한 데이터만 가능
        - String, Integer, float, boolean, tuple, range
- 각 키의 값
    - 어떠한 형태든 관계없음
    

### 딕셔너리 메서드

1. `d.clear()` : 모든 항목 삭제
2. `d.copy()` : 딕셔너리 d의 얕은 복사본을 반환
3. `d.keys()` : 딕셔너리 d의 모든 키를 담은 뷰를 반환
4. `d.values()` : 딕셔너리 d의 모든 값을 담은 뷰를 반환
5. `d.items()` : 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환

<h4> <mark>조회</mark> </h4>

1. <mark>d.get(k[, default]) : 키 k의 값을 반환하는데, **키 k가 딕셔너리 d에 없는 경우, None을 반환**</mark>
2. d.get(k, v) : 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환
    
    ```python
    my_dict = {'apple':'사과', 'banana':'바나나'}
    my_dict['pineapple'] # KeyError : 'pineapple'
    
    my_dict = {'apple':'사과', 'banana':'바나나'}
    print(my_dict.get('pineapple')) # None
    print(my_dict.get('apple')) # 사과
    print(my_dict.get('pineapple', 0)) # 0 디폴트 값 설정
    ```
    ```python
    def count_blood(blood_list):
        result = {}
        for blood in blood_list:
            '''1.
            if result.get(blood):
                result[blood] += 1
            else:
                result[blood] = 1
            '''
            result[blood] = result.get(blood, 0) + 1

    ```

<h4> <mark>추가 및 삭제</mark> </h4>

1. `d.pop()` : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 d에 없는 경우 KeyError 발생
2. `d.pop(k[, default])` : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 d에 없는 경우 v를 반환
    
    ```python
    my_dict = ('apple':'사과', 'banana':'바나나'}
    data = my_dict.pop('apple')
    print(data, my_dict) # 사과 {'banana':'바나나'}
    
    my_dict = ('apple':'사과', 'banana':'바나나'}
    data = my_dict.pop('pineapple') 
    print(data) # KeyError : 'pineapple'
    ```
    
3. `d.update([other])` : 딕셔너리 d의 값을 매핑하여 업데이트
    
    ```python
    my_dict = {'apple':'사', 'banana':'바나나'}
    my_dict.update(apple = '사과')
    print(my_dict) # {'apple':'사과', 'banana':'바나나'}
    ```
    

---