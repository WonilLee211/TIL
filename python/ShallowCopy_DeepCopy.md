# 얕은 복사와 깊은 복사

- Shallow Copy & Deep Copy
> **주의**
> - 얕은 복사의 정의는 변수를 복사할 때 객체의 요소 값이 아닌 동일한 메모리 주소에서 참조하는 현상을 말합니다.
> - 하지만 파이썬 공식문서에서는 위와 같은 현상을 해결하고자 인덱스 슬라이싱, copy모듈의 copy함수, list() 등의 방법도 얕은 복사라 명명합니다.
> - 왜냐하면 이중 리스트의 경우 위 방법 또한 얕은 복사가 발생하기 때문으로 추측됩니다.

## 복사방법

1. 할당(assignment)
2. 얕은 복사(Shallow Copy)
4. 깊은 복사(Deep Copy) : copy모듈 사용

- 변경 불가능한 데이터에 대해서 얕은 복사가 일어나지 않습니다.
    - 리터럴(숫자, 글자, 참거짓)
    - range()
    - tuple()
    - frozenset()
- 변경가능한 mutable 데이터에 대해서 얕은 복사가 발생합니다.
    - 리스트
    - dict
    - set


## 할당(assignment)

- 대입 연산자(=) : 해당 객체에 대한 객체 참조를 복사
    
    ```python
    original_list = [1, 2, 3]
    copy_list = original_list # 해당 오리지널에 대한 주소를 카피에 복사
    print(orginal_list, copy_list) # [1, 2, 3] [1, 2, 3]
    
    copy_list[0] = 'hello'
    print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]
    ```
    
- <mark>얕은 복사 : 실제 요소값이 아닌 해당 객체의 참조(주소)를 복사</mark>
    - 해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향을 끼친다.

## 얕은 복사 해결

- slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사(다른 주소)
    
    ```python
    a = [1, 2, 3]
    b = a[:]
    print((a, b) # [1, 2, 3] [1, 2 ,3]
    b[0] = 5
    print(a, b) # [1, 2, 3] [5, 2 ,3]
    ```
    
- <mark>인덱스 슬라이싱의 주의사항</mark>
    1. 복사하는 리스트의 원소가 주소를 참조하는 경우
        ```python
        a = [1, 2, ['a', 'b']]
        b = a[:] # 슬라이싱해서 원본을 저장하는 것.
        print((a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
        b[2][0] = 0
        print(a, b) # [1, 2, [0, 'b']] [1, 2, [0, 'b']]
        ```
        

## 깊은 복사(Deep Copy)

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
b[2][0] = 0
print(a, b) # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
```