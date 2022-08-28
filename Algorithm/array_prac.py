import sys, pprint
sys.stdin = open('input.txt')

# 페인트 칠을 모두 끝낸 후, 전체 벽에서 가장 넓은 영역을 차지하고 있는
# 명도 번호를 찾고 해당 명도 번호가 차지하고 있는 영역의 크기를 구하기

def painting():
    for info in painting_info:
        frm_r, frm_c, to_r, to_c, clr = info

        for i in range(frm_r, to_r + 1):
            for j in range(frm_c, to_c + 1):
                if wall[i][j] < clr:
                    wall[i][j] = clr

    pprint.pprint(wall)

    scales = [0] * 11
    for i in range(1, 11):
        for row in wall:
            scales[i] += row.count(i)
    # [0, 10, 8, 6, 21, 4, 0, 0, 0, 0, 0]
    max_idx = 0
    for i in range(1, 11):
        if scales[i] > scales[max_idx]:
            max_idx = i

    return max_idx, scales[max_idx]

if __name__ == '__main__':
    n, m = map(int, input().split())
    wall = list([0] * m for _ in range(n))

    painting_info = [0] * 11
    for i in range(11):
        frm_r, frm_c, to_r, to_c, clr = map(int, input().split())
        painting_info[i] = [frm_r, frm_c, to_r, to_c, clr]

    result = painting()

    print(result[0], result[1])
