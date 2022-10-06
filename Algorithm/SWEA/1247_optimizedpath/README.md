# SWEA D5 1247 최적 경로

## 문제

회사에서 고객들을 방문하고 자신의 집으로 돌아가는 경로 중 가장 짧은 경로 찾기
---

## 입력

- 첫번째 줄 : 테스트 수
- 테스트 케이스 첫번째 줄 : 고객의 수
- 테스트 케이스 두번째 줄 : 집 위치, 회사위치, 고객 위치의 (x,y)

---

## 출력

- "#(testcase) (최단 경로의 이동거리)" 형태

---

## 제약

---

## 알고리즘

1. 테스트케이스 수 정보 저장
2. 테스트 케이스별로 집, 회사, 고객 위치를 리스트에 저장
3. 집, 회사 정보 따로 빼내기
4. permultations 순열함수 사용하기
   1. 리스트 슬라이스를 통해 path변수에 회사-고객-집 순의 조합 만들기
   2. 고객 위치를 permultations함수를 통해 순열로 모든 경우 구하기
   3. 각 경우의 path마다 거리 계산하기
   4. 최소의 거리 조건 달기. 