import sys
sys.stdin = open('input.txt')
from collections import deque
from pprint import pprint
for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    # r, c,  미생물 수, 이동방향
    orgs = {i:list(map(int, input().split())) for i in range(1, k + 1)}
    di = {1:-1, 2:1, 3:0, 4:0}
    dj = {1: 0, 2:0, 3:-1, 4:1}
    d = [0, 2, 1, 4, 3]
    visited = [ [ 0 for _ in range(n)] for i in range(n)]

    cnt = 0
    while cnt < m:
        print(orgs[1])
        keys = list(orgs.keys())
        for j in keys:
            orgs[j][0], orgs[j][1] = orgs[j][0] + di[orgs[j][3]], orgs[j][1] + dj[orgs[j][3]]
            if orgs[j][0] == 0 or orgs[j][0] == n-1 or orgs[j][1] == 0 or orgs[j][1] == n-1:
                orgs[j][3] = d[orgs[j][3]]
                orgs[j][2] = orgs[j][2] // 2
                if orgs[j][2] == 0:
                    del orgs[j]
        print(visited)
        keys = list(orgs.keys())
        for j in keys:
            if visited[orgs[j][0]][orgs[j][1]]:
                print(visited)
                temp = [[], []]
                for k in keys:
                    if orgs[j][0] == orgs[k][0] and orgs[j][1] == orgs[k][1]:
                        temp[0].append(orgs[k][2])
                        temp[1].append((orgs[k][3], k))
                orgs[j][2] = sum(temp[0])
                orgs[j][3] = temp[1][temp[0].index(max(temp[0]))][0]
                for t in sorted(temp[1])[1:]:
                    del orgs[t[1]]
                # org1 = orgs[visited[orgs[j][0]][orgs[j][1]]]
                # if org1[2] > orgs[j][2]:
                #     orgs[visited[orgs[j][0]][orgs[j][1]]][2] += orgs[j][2]
                #     del orgs[j]
                # else:
                #     orgs[j][2] += orgs[visited[orgs[j][0]][orgs[j][1]]][2]
                #     del orgs[visited[orgs[j][0]][orgs[j][1]]]
                #     visited[orgs[j][0]][orgs[j][1]] = j

            else:
                visited[orgs[j][0]][orgs[j][1]] = j

        pprint(visited)
        print()

        cnt += 1
        visited = [[0 for _ in range(n)] for k in range(n)]

    total = 0
    for k, v in orgs.items():
        print(k, v)
        total += v[2]
    print(f'#{tc} {total}')