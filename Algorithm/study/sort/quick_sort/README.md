# 퀵정렬
<h6>참조 : https://www.daleseo.com/sort-quick/</h6>
<h2>개념</h2>

- 분할 정복(divide and conquer) 알고리즘 중 하나
- 재귀함수 이용
- 피봇(pivot)이라는 임의의 기준값을 설정(보통 중앙값으로 함. 가장 빠름)
- 피본을 기준으로 큰 값(오른쪽) 작은 값(왼쪽)으로 나눔(정렬)
    - 정렬 후 오른쪽과 왼쪽은 비교할 필요가 없음

<h2>특징</h2>

- 파이썬이나 자바에서 제공되는 built-in 메서드 sort()는 퀵정렬 기본
- 분할 시점부터 비교연산이 일어나기 때문에 그 이후 병합에 들어가는 비용이 매우 적거나 구현 방법에 따라서 아예 병합을 하지 않을 수 있습니다.
- 구현 방법에 따라 공간복잡도가 달라질 수 있음
- 입력 배열이 차지하는 메모리만을 사용하는 in-place sorting 방식을 구현할 경우, O(1)의 공간복잡도를 가진 코드의 구현이 가능하다.

  ![Alt text](../../../img/mergesort.PNG)
  
  <h6>출처 :  </h6>
---
<h2>알고리즘</h2>
오름차순
1. 피봇 설정
2. 피봇보다 크면 오른쪽 작으면 왼쪽 리스트에 저장
3. 피봇은 mid리스트에 저장
4. 각 리스트로 퀵 함수 재호출함과 동시에 합치기

---

<h2>예시 코드</h2> 
<details>
<summary> </summary>
<div markdown="1">

```python
def quick_sort(arr):
  if len(arr) <2:
    return arr

  fvt_idx = len(arr)//2
  leftlist, midlist, rightlist = [], [arr[fvt_idx]], []

  for el in arr:
    if arr[fvt_idx] > el:
      leftlist.append(el)
    elif arr[fvt_idx] < el:
      rightlist.append(el)

  return quick_sort(leftlist) + quick_sort(midlist) + quick_sort(rightlist)

```

</div>
</details>

---

<h2>장단점</h2>

- 장점
  - 기본적인 정렬의 상용코드가 퀵정렬방식을 채택

- 단점
  - 공간복잡도가 크다.(상용화되는 코드에서 메모리 사용 과다는 심각한 문제)
  - fivot 선택 방식에 따라 성능 차이가 크다.
---

<h2>퀵 정렬 개선 </h2>


---

<h2>예시 코드</h2> 
<details>
<summary> </summary>
<div markdown="1">

```python


```





<h2> 복잡도 </h2>
- 이상적인 경우 O(nlogn)
- 최악의 경우 O(n**2)
<details>
<summary> </summary>
<div markdown="1">



</div>
</details>


---