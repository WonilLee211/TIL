# 선택정렬 selection sort

<h2>개념</h2>

- 가장 작은 값을 찾아서 첫 번째 자리에 놓고 그 다음 작은 값을 2번째 자리에 놓으며 정렬
  ![Alt text](../../../img/selectionsort.PNG)
  
  <h6>출처 :https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html</h6>

<h2>시간복잡도</h2>

  -  비교횟수 : (시퀀스 요소 개수-1)*(시퀀스 요소 개수 -2)/2 >> O(n**2)
  -  교환횟수 : 3(n-1)

<h2>알고리즘</h2>
1. **오름차순**
   
   - 배열 중 최댓값을 인덱스 0번자리와 교환
   - 배열 중 두 번째 최댓값을 인덱스 1번 자리와 교환
     ...

2. **내림차순**
   
   - 배열 중 최솟값을 인덱스 0번자리와 교환
   - 배열 중 두 번째 최솟값을 인덱스 1번 자리와 교환
     ...

---

<h2>예시 코드</h2> 
<details>
<summary> </summary>
<div markdown="1">

```python
def selection_sort(data, increasing = True):
    #오름차순
    if increasing == True:

        for i in range(len(data)-1):
            max_idx = i

            for j in range(i+1, len(data)):               
                if data[max_idx] < data[j]:
                    max_idx = j

            data[max_idx], data[i] = data[i], data[max_idx]

    # 내림차순
    else:
        for i in range(len(data)-1):
            min_idx = i

            for j in range(i+1, len(data)):               
                if data[min_idx] > data[j]:
                    min_idx = j
            data[min_idx], data[i] = data[i], data[min_idx]

    return data

if __name__ == '__main__':
    numbers = [7, 4, 11, 9, 2]

    print(selection_sort(numbers))
    print(selection_sort(numbers, increasing = False))
```

</div>
</details>

---

<h2>장단점</h2>

- 장점
  1. 개념이 단순해서 프로그래밍하기 쉽습니다.
- 단점
  1. 비교작업이 너무 많아서 연산 시간이 오래 걸리는 편입니다.
  2. 대량의 데이터에 버블정렬을 적용하면 집에 못갑니다.
  3. 버블정렬처럼 플래그를 활용하여 작업 도중에 최적값을 찾았을 때 반복을 맘출 수 없습니다.

---
