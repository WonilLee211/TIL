'''
상자들이 쌓여있는 방이 있다.
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 
낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램
'''

arr = list(map(int, input().split()))
# 요소별로 자신보다 큰 인덱스 위치의 다른 요소보다 크다면 낙차 + 1/ 작다면 낙차 + 0
# 낙차가 가장 큰 곳은 항상 컬럼의 꼭대기

max_dy = 0
crt_dy = 0

N = 0
for _ in arr:
    N += 1

for i in range(N):
    for height in arr[i+1:]:
        # # i번째 컬럼 꼭대기 층 box가 다른 컬럼의 높이보다 크다면 
        if arr[i] > height:
            crt_dy += 1 # 낙차 + 1
    if crt_dy > max_dy: # 비교 후 낙차가 max_dy보다 크다면 max_dy 최신화
        max_dy = crt_dy
    # i컬럼의 비교가 끝나면 crt_dy 초기화
    crt_dy = 0

print(max_dy)