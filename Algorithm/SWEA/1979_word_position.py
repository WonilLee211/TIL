'''
주어진 매트릭스에서 단어가 들어갈 수 있는 빈 공간을 행과 열방향으로 구하기
'''
from functools import reduce


# 행마다 x축 방향으로 글자 수와 동일한 공간 세기
def cnt_space(matrix, k):
    # 행별로 0으로 나눠서 1, 111.. 형태로 저장
    temp_puzzle = list(list(row.split('0')) for row in matrix)
    needed_space = '1' * k
    cnt = 0

    for row in temp_puzzle:
        for space in row:
            # 길이가 일치하면 카운트
            if space == needed_space:
                cnt += 1

    return cnt

# 전치행렬 만들기
def oppositeangle_symmetry(matrix, n):
    temp_matrix = list()

    for i in range(n):
        new_row = ''

        for j in range(n):
            new_row += matrix[j][i]
        temp_matrix.append(new_row)

    return temp_matrix

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    result = 0
    data = list(list(input().split()) for _ in range(N))
    # reduce함수를 이용하여 입력값을 문자열형태의 단일 리스트로 만들기 ex> ['10111', ...]
    puzzle = list(reduce(lambda acc, num: acc + num, data[i]) for i in range(N))

    result += cnt_space(puzzle, K) #행방향 공간 계산
    result += cnt_space(oppositeangle_symmetry(puzzle, N), K) # 열방향 공간 계산

    print(f"#{tc} {result}")