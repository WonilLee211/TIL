import sys
sys.stdin = open('input.txt')

'''
G : 탑승구 수 1 <= g < 100,000
P : 비행기 수 1 <= p < 100,000
도킹할 수 있는 탐승구 번호 : p개 줄
 - i번째 비행기가 1번부터 gi번째 탑승구 중 하나에 도킹할 수 있다는 의미

출력
- 도킹할 수 있는 비행기 최대 개수

논리
- 각 비행기별로 연결될 수 있는 탑승구를 연결리스트로 표현



'''


import sys
input = sys.stdin.readline

