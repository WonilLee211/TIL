import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n = int(input()) # 원자의 수
    atoms = [0] * n
    for i in range(n):
        atoms[i] = list(map(int, input().split()))
    # x, y, m, k
    # [[-1000, 0, 3, 5], [1000, 0, 2, 3], [0, 1000, 1, 7], [0, -1000, 0, 9]]

    # 상0하1좌2우3
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    colliding = True
    energy = 0
    while colliding:
        visiting = {}

        # 위치 업데이트
        for i in range(n):
            if not atoms[i]:
                continue
            atoms[i][0], atoms[i][1] = atoms[i][0] + dx[atoms[i][2]], atoms[i][1] + dy[atoms[i][2]]

        for i in range(n):
            if not atoms[i]:
                continue
            if (atoms[i][0], atoms[i][1]) not in visiting.keys():
                visiting[(atoms[i][0], atoms[i][1])] = i
            else:
                energy += atoms[i][-1]
                if atoms[visiting[(atoms[i][0], atoms[i][1])]]:
                    energy += atoms[visiting[(atoms[i][0], atoms[i][1])]][-1]
                    atoms[visiting[(atoms[i][0], atoms[i][1])]] = 0
                atoms[i] = 0

        # 내가 가는 방향에 있는 원자들 중 방향이 다른 원자가 없을 때 충돌 가능성 zero
        # 내가 가는 방향에 있는 원자들 중 방향이 다르고 인덱스 차이의 절대값이 같을 때
        colliding = False
        for i in range(n):
            if not atoms[i]:
                continue
            atom = atoms[i]
            flag = False
            for j in range(n):
                if not atoms[j]:
                    continue
                atom1 = atoms[j]
                if atom[2] == 0:
                    if atom1[2] in [2, 3] and atom1[1] > atom[1] and abs(atom[1] - atom1[1]) == abs(atom1[0] - atom[0]):
                        colliding = True
                        flag = True
                        break
                    elif atom1[2] == 1 and atom1[1] > atom[1] and atom[0] == atom1[0]:
                        colliding = True
                        flag = True
                        break
                if atom[2] == 1:
                    if atom1[2] in [2, 3] and atom1[1] < atom[1] and abs(atom[1] - atom1[1]) == abs(atom1[0] - atom[0]):
                        colliding = True
                        flag = True
                        break
                    elif atom1[2] == 0 and atom1[1] < atom[1] and atom[0] == atom1[0]:
                        colliding = True
                        flag = True
                        break
                if atom[2] == 2:
                    if atom1[2] in [0, 1] and atom1[0] < atom[0] and abs(atom[1] - atom1[1]) == abs(atom1[0] - atom[0]):
                        colliding = True
                        flag = True
                        break
                    elif atom1[2] == 3 and atom1[0] < atom[0] and atom[1]  == atom1[1]:
                        colliding = True
                        flag = True
                        break
                if atom[2] == 3:
                    if atom1[2] in [0, 1] and atom1[0] > atom[0] and abs(atom[1] - atom1[1]) == abs(atom1[0] - atom[0]):
                        colliding = True
                        flag = True
                        break
                    elif atom1[2] == 2 and atom1[0] > atom[0] and atom[1] == atom1[1]:
                        colliding = True
                        flag = True
                        break

            if flag:
                break

    print(f'#{tc} {energy}')

