'''
기둥은 바닥위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 함.
보는 한쪽 끝부분이 기둥 위에 있더나 끝부분이 다른 보와 동시에 연결되어 있어야 함

building frame의 세로 길이  1 ~ 1000
buliding frame의 가로 길이 4

building frame [x, y, a, b]
보 또는 기둥을 설치 삭제할 교차점의 좌표
a : 기둥 0, 보 1
b : 삭제 0, 설치 1
교차점을 기준으로 위로 또는 오른쪽으로 설치 또는 삭제해야 함

Return은 가로 길이가 3인 2차원 배열로 각 구조물의 좌표를 담아야 함
[x, y, a]
return 오름차순 정렬하기

논리
- 기둥 설치 가능 경우
    - 바닥위에 있는 경우 / r = 0
    - 보의 한쪽 끝부분 위에 있음 / beam(r, c - 1) = 1 or beam(r, c) = 1
    - 기둥 위에 있어야 함 / bar(r - 1, c) = 1
- 보 설치 가능 경우
    - 한쪽 끝 부분이 기둥 위에 있는 경우 / bar(r - 1, c) = 1 or bar(r -1, c + 1) = 1
    - 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 함 / beam(r, c - 1) = bream(r, c + 1) = 1
- 기둥 삭제 가능 경우
    - 해당 위치 삭제 후 모든 점에 대해서 설치가능한지 확인
        - 불가능하면 해당 위치 설치
- 보 삭제 가능 경우
    - 해당 위치 삭제 후 설치한 점들에 대해서 설치 가능한지 확인
        - 불가능하면 해당 위치 다시 설치
'''
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

installed_bar = [[0] * (n + 1) for i in range(n + 1)]
installed_beam = [[0] * (n + 1) for i in range(n + 1)]

def is_possible(r, c, a):
    if a:   # 보일 때
        if installed_bar[r - 1][c] or installed_bar[r - 1][c + 1] or (c != 0 and installed_beam[r][c - 1] and installed_beam[r][c + 1]):
            return True
        return False
    else: # 기둥일 때
        if r == 0 or installed_beam[r][c - 1] or installed_beam[r][c] or installed_bar[r - 1][c]:
            return True
        return False

ans = set()

for c, r, a, b in build_frame:
    if b:
        if is_possible(r, c, a):
            if a:
                installed_beam[r][c] = 1
            else:
                installed_bar[r][c] = 1
            ans.add((c, r, a))

    else: # 삭제일 때
        ans.remove((c, r, a))
        if a == 1:
            installed_beam[r][c] = 0
        else:
            installed_bar[r][c] = 0

        for c_, r_, a_ in ans:
            if not is_possible(r_, c_, a_):
                ans.add((c, r, a))
                if a:
                    installed_beam[r][c] = 1
                else:
                    installed_bar[r][c] = 1
                break

ans = list(map(list, sorted(list(ans))))
print(ans)