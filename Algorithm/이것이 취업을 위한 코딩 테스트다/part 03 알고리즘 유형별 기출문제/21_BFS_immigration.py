import sys
sys.stdin = open('input.txt')


'''
2500 4 = 10000

반복마다 인접리스트 만들기

국경선을 공유하는 두 나라의 인구차이가 L <= <= R일 때 두나라가 공유하는 국경선을 오늘 하루 동안 연다
열려야하는 국경선이 모두 열렸다면 인구 이동 시작
국경선이 열려있으면 하루동안 연합
연합을 이루고 각 칸의 인구수는 (연합의 인구수 / 연합을 이루고 있는 칸의 개수)
인구이동이 발생하는 횟수 출력
- 하루동안 연합이 한번이라도 발생하면 count
- 없으면 pass

1. visited 하지 않은 위치부터 연합국 만들기   
    - bfs
    - visited 표시하기
2. 다음 연합국만들기
    - visited 하지 않은 곳에서 시작
3. 다돌았으면 연합국 만들기가 한번이라도 표시됐는지 확인
    - COUNT
4.  



'''

import sys, collections
input = sys.stdin.readline
deque = collections.deque
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

n, L, R = map(int, input().split())
land = [list(map(int, input().split())) for i in range(n)]



def is_possible(r, c, nr, nc):
    global L, R
    return True if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and L <= abs(land[nr][nc] - land[r][c]) <= R else False

def bfs(i, j):
    union = []
    q = deque()
    q.append((i, j))
    union.append((i, j))
    visited[i][j] = True

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if is_possible(r, c, nr, nc):
                visited[nr][nc] = True
                q.append((nr, nc))
                union.append((nr, nc))

    return union

def immigration(i, j):
    union = bfs(i, j)

    if len(union) == 1:
        return False

    population = 0
    cnt_country = len(union)

    for r, c in union:
        population += land[r][c]

    average = population // cnt_country

    for r, c in union:
        land[r][c] = average

    return True

ans = 0


while True:
    flag = 0
    visited = [[False] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and immigration(i, j):
                flag += 1

    if flag > 0:
        ans += 1
    else:
        break

print(ans)

