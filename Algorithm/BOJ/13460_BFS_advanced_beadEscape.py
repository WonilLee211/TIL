'''
빨간공과 파란공이 보드에 있을때 빨간 공만 빼내기 위한 최소의 기울이기 동작 횟수

논리
- 네 가지의 기울임마다 빨간공과 파란공이 움직임
- 기우렸을 때 동작의 경우
    1. 벽을 나는 경우
    2. 빨간공이 출구를 만나는 경우
    3. 파란공이 출구를 만나는 경우
    4. 한번의 기울임으로 두 공이 출구로 빠지는 경우
    5. 빨간공과 파란공이 만나는 경우

- bfs
- 모든 방향의 기울임을 한번씩 해본다.
- 10번안에 안끝나면 break
- 그전에 찾으면 break
- 파란공이 구멍에 들어가지 않았고 이전의 기울임과 다른 기울임을 선택하고
- 기울인 방향으로 #이나 공이 없을 때까지 움직여 위치바꾸기
- 이후 q에 빨간공 파란공 위치와 횟수 저장
- 동시에 탈출한 경우를 어떻게 처리할까.
    - 동시에 탈출하던 파란공만 탈출하던 탈출하면 그 케이스 버리기
- 파란공과 빨간공을 어떻게 이동시킬까
    - 한칸씩 이동시키면서 O 인지 . 인지 확인
'''
import sys
sys.stdin = open('input.txt')


from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

red, blue, hole = [0, 0], [0, 0], [0, 0]

for r in range(n):
    for c in range(m):
        if board[r][c] == 'B':
            blue = [r, c]
            board[r][c] = '.'
        elif board[r][c] == 'R':
            red = [r, c]
            board[r][c] = '.'
        elif board[r][c] == 'O':
            hole = [r, c]

tilting = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

cnt = 11
q = deque()
q.append([red[0], red[1], blue[0], blue[1], 0, 4])

while q:
    rr, rc, br, bc, count, tilt = q.popleft()

    if count == 10: # 10회동안 탈출 못하면 그 케이스 버리기
        continue

    if count > cnt: # count가 현재 가장 작은 cnt보다 크면 버리기
        continue

    for i in range(4):
        if i == tilt:   # 이전에 기울였던 방향이면 선택 안하기
            continue

        new_rr, new_rc, new_br, new_bc = rr, rc, br, bc
        t = tilting[i]

        # 구슬 이동 로직
        Rflag = Bflag = True # 두 구슬의 움직임 여부 표시
        while Rflag or Bflag:
            Rflag = Bflag = False  # 두 구슬의 움직임 여부 표시

            if board[new_rr + t[0]][new_rc + t[1]] == 'O':  # 가려는 방향이 탈출구면 무조건 진행
                new_rr, new_rc = new_rr + t[0], new_rc + t[1]
                Rflag = True
            # 가는 방향이 탈출구가 아니고, 다른 구슬이 없고, 현재 위치가 탈출구가 아니고, 다음 위치가 . 일 때 이동
            elif (new_rr + t[0] != new_br or new_rc + t[1] != new_bc) and board[new_rr][new_rc] != 'O' and board[new_rr + t[0]][new_rc + t[1]] == '.':
                new_rr, new_rc = new_rr + t[0], new_rc + t[1]
                Rflag = True

            # 상동
            if board[new_br + t[0]][new_bc + t[1]] == 'O':
                new_br, new_bc = new_br + t[0], new_bc + t[1]
                Blag = True
            elif (new_rr != new_br + t[0] or new_rc != new_bc + t[1]) and board[new_br][new_bc] != 'O' and board[new_br + t[0]][new_bc + t[1]] == '.':
                new_br, new_bc = new_br + t[0], new_bc + t[1]
                Bflag = True

        # 파란 구슬이 탈출구에 들어간 케이스 버리기
        if board[new_br][new_bc] == 'O':
            continue
        # 파란 구슬이 탈출구에 들어가지 않았고 빨간 구슬만 탈출구에 들어간 경우
        elif board[new_rr][new_rc] == 'O':
            if count + 1 < cnt:     # count + 1가 지금 cnt보다 작으면 갱신
                cnt = count + 1
        else:
            q.append([new_rr, new_rc, new_br, new_bc, count + 1, i])

if cnt == 11:
    print(-1)
else:
    print(cnt)