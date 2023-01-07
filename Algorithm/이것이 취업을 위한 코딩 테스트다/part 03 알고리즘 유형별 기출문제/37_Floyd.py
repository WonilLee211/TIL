import sys
sys.stdin = open('input.txt')

'''
n(2 ≤ n ≤ 100)개의 도시
m(1 ≤ m ≤ 100,000)개의 버스
 - 한 도시에서 출발하여 다른 도시에 도착
 
모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성

입력
n
m
a, b, c = from, to, 비용
1 <= c <= 100000

시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다. 양방향이라는 뜻?

dp로 갈 수 있는 모든 곳 방문

INF로 남아 있는 값은 0으로 변경 후 출력

'''
import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())

board = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m): # 간선 정보 저장
    a, b, c = list(map(int, input().split()))
    board[a][b] = min(board[a][b], c)

for i in range(n + 1):
    board[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == INF:
            print(0, end=" ")
        else:
            print(board[i][j], end=" ")
    print()

