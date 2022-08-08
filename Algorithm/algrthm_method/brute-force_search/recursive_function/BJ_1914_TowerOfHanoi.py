# 하노이 탑
# 1 번탑에 쌓인 블럭을 3번 탑으로 옮기는 횟수와 이동경로
'''
알고리즘
횟수는 2**n-1 의 규칙성을 보임
이동은 재귀함수를 통한 완전탐색
함수는 x 탑에서 z탑으로 옮기는 함수
1. n개의 블럭이 z탑으로 가기 위해 
 1.1 n-1개의 블럭이 y탑으로 옮기기
 1.2 n번째 블럭을 z탑으로 옮기기
 1.3 y탑을 n-1개의 블럭 z탑으로 옮기기
2. 탈출 조건 n==1일 때 print(a, c)
'''
# N개의 블럭이 x탑에 있을 때 z탑으로 옮기는 함수
def hanoi(x, y, z, N):
    if N == 1:
        print(x, z, sep=" ")
        return
    
    hanoi(x, z, y, N-1)
    hanoi(x, y, z, 1)
    hanoi(y, x, z, N-1)

N = int(input())

print(2**N - 1)
if N <= 20:
    hanoi(1, 2, 3, N)