import sys
sys.stdin = open('input.txt')

'''
1 ~ n 번 도시
한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 순회 여행 경로
한 번 갓던 도시로는 다시 못감
가장 적은 비용을 들이는 여행 계획 구하기

W[i][j] :각 도시 i에서 도시 j로 이동하는데 드는 비용 행렬(비대칭)
- 갈 수 없는 경우 W = 0

1초면 20만번 연산 허용

논리
- 모든 지점에서 출발해서 최소 비용
- 사이클을 만들어야 함.
- 조건 마지막 도시b는 첫 도시a와 연결되어있어야 함.
    - w[b][a] != 0

모든 순열을 구하는건 시간초과 : 1307674368000

비트필드를 이용한 다이나믹 프로그래밍

'''
n = int(input())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

