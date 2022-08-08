# 2. 카운팅 정렬

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여 선형 시간에 정렬하는 효율적인 알고리즘

## 특징

- 비교환식 방식
- 단점 : n이 비교적 작을 때만 가능하다.

## 제한사항

- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
- 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스되는 카운트들의 배열을 사용하기 때문
- 카운트들을 위한 충분한 공간을 할당하려면 집합 내에 가장 큰 정수를 알아야 함

## 시간복잡도

- O(n + k) : n은 리스트의 길이, k는 정수의 최대값

## 알고리즘

- 배열 내에 최대값만큼의 인덱스를 가진 count 리스트 생성
- 배열의 값을 count 리스트 인덱스위치에 +1
- count 리스트 요소를 오름차순으로 누적합 적용
- temp 리스트 생성
- 원본 데이터를 뒤에서부터 요소를 읽어나가며 요소의 값을 count리스트에서 인덱스로 사용하여 해당 위치의 값에 -1하고 결과값을 temp 리스트의 인덱스로 사용하여 요소를 저장

```python
def countingsort(arr, N):
    max_num = 0
    # arr에서 최대값 구하기
    for num in arr:
        if num > max_num:
            max_num = num:
    
    temp_arr = [0 for _ in range(N)]
    cnt_arr = [0 for _ in range(max_num + 1)] # 최대값의 인덱스를 갖는 카운팅 리스트 만들기
    
    # 배열의 요소값을 인덱스로 사용해서 cnt_arr에 갯수 세기
    for num in arr:
        cnt_arr[num] += 1
    # cnt_arr를 누적합 시키기
    for i in range(1, max_num + 1):
        cnt_arr[i] += cnt_arr[i-1]
    # cnt_arr를 의 값을 인덱스로 사용해서 temp_arr에 arr의 뒤쪽 요소부터 배열하기
    for i in range(N-1, 0, -1):
        cnt_arr[arr[i]] -= 1
        temp_arr[cnt_arr[arr[i]]] = arr[i]
```