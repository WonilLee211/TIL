import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split())
target = int(input()) # i + j -1 의 위치만 알아 내면 된다.

# c + 2 * r +2 매트릭스 만들기
matrix = [[0] * (c +2)]
for i in range(r):
    temp = [0] + [1]*c + [0]
    matrix.append(temp)
matrix.append([0] * (c +2))
matrix[1][1] = 0

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

order = 1
pstion = [1, 1]

if target == 1:
    print(*[1, 1])

elif target > r*c:
    print(0)
else:
    while order != target:
        for move in moves:
            while True:
                tempx, tempy = pstion[0] + move[0], pstion[1] + move[1]
                if matrix[tempx][tempy] == 1:
                    order += 1
                    pstion[0] += move[0]
                    pstion[1] += move[1]
                    matrix[pstion[0]][pstion[1]] = order
                    if order == target:
                        break
                else:
                    break

            if order == target:
                break

    print(*pstion)