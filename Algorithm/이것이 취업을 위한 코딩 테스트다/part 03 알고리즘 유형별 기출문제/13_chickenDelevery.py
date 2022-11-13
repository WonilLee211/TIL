'''

2 : 치킨
1 : 집
0 : 빈칸
치킨 거리 : 집과 가장 가까운 치킨 집 사이 거리

M개의 치킨집을 골라 치킨거리가 가장 작게 되는 구하는 프로그램
M개의 치킨집의 치킨 거리 최소값

논리
- M 개 이하의 치킨집 조합별로 도시의 치킨 거리 합의 최소 구하기
- 완전 탐색
- 조합 1 ~ M 개
- 백트래킹 조건 : 현재 구한 최소 치킨 거리 합보다 크면 break

주의
- 거리 초기값 설정이 생각보다 작아서 에러 발생

'''
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

# 치킨집 위치 구하기'
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chickens.append((i, j))
            board[i][j] = 0

        elif board[i][j] == 1:
            houses.append((i, j))

num = len(chickens)
# 1이상 M 이하의 조합 만들기

res = 2 * n * num

for i in range(1, 1<<num):
    case = []

    for j in range(num):
        if i & (1 << j):
            case.append(j)
    if len(case) > m:
        continue

    distance = 0
    for home in houses:
        home_dis = 1000000000000
        for idx in case:
            store = chickens[idx]
            home_dis = min(home_dis, abs(home[0] - store[0]) + abs(home[1] - store[1]))
        distance += home_dis

        if distance > res:
            break

    if distance < res:
        res = distance

print(res)