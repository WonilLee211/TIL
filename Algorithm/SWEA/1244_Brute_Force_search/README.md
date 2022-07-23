# SWEA D3 1244 최대 상금

## 문제

입력받은 숫자열을 교환 횟수만큼 교환하고 얻을 수 있는 최댓값 출력하기
---

## 입력

- 첫번째 줄 : 테스트 수
- 테스트 케이스 첫번째 줄 : 숫자열, 교환 횟수

---

## 출력

- "#(testcase) (가능한 최댓값)" 형태

---

## 제약

- 정점의 크기는 부모 자식 관계와 무관
- 주어지는 두 정점이 서로 조상과 손자인 관계인 경우는 없다.

---

## 알고리즘

완전 탐색으로 모든 경우의 수를 구하고 그 중에서 가장 큰 값 출력하기
1. 숫자열 입력받기
2. 허용되는 횟수만큼 반복
    1. 입력받은 숫자열에 대해서 o번째 숫자와 1~ 끝까지 한번씩 교환
    2. 리스트에 저장
    3. 다음 교환해볼 대상으로 저장
    4. 1번으로 돌아가기

## 애로사항
메모리 초과로 오답
개선 : 최대값이 중간에 발견되면 반복 중지하도록 코드 추가

```python
T = int(input())
for testcase in range(1, T+1):

    str_num, K = input().split()

    # 입력받은 str_num의 최대값인 경우 찾기
    li = list(int(s) for s in str_num)
    li = sorted(li, reverse = True)
    maxvalue = ''
    for n in li:
        maxvalue += str(n)
    # 입력받은 숫자열 amxvalue

    length = len(str_num)
    
    numlist = []
    numlist.append(str_num)

    cnt = 0      
    while cnt != int(K): # 반복가능한 횟수만큼
        cnt += 1
        caselist = [] # 반복 1회당 가능한 경우의 숫자열 저장장소
        for number in numlist: # ['12123', 31212'..] 형태 
            
            # 숫자 두 개를 골라서 교환하는 모든 경우의 수 구하기
            for i in range(length):
                for j in range(i + 1,length):
                    temp = list(number)
                    temp[i], temp[j] = temp[j], temp[i]
                    
                    case =''
                    for k in range(length):
                        case += temp[k]
                    
                    caselist.append(case)
        # 다음 반복에서 교환할 숫자열 리스트 최신화
        numlist = caselist

        # 반복 과정에서 maxvalue 찾았다면 stop
        if str(maxvalue) in numlist:
            break
    
    # 숫자열을 정수 타입으로 변경
    numlist = [int(num) for num in numlist]

    print(f"#{testcase} {max(numlist)}")
```