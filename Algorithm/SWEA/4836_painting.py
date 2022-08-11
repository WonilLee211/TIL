'''
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램.
'''
def painting(paint_info, N):
    # 색칠할 공간
    grid = list([''*10 for _ in range(10)] for _ in range(10))

    # 색칠하기
    for i in range(N):
        from_y, from_x, to_y, to_x, color = paint_info[i]
        for r in range(to_y - from_y + 1):
            for c in range(to_x - from_x + 1):
                # 색칠을 문자열 형태로 저장 ex> '112'
                grid[from_y + r][from_x + c] += str(color)

    cnt = 0
    for i in range(10):
        for j in range(10):
            # 색칠을 12 순서나 21순서로 했을 때 경우 cnt 1
            if '12' in grid[i][j] or '21' in grid[i][j]:
                cnt += 1

    return cnt

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N_ = int(input())
        paint_info_ = []
        for i in range(N_):
            paint_info_.append(list(map(int, input().split())))
        print(f"#{test_case} {painting(paint_info_, N_)}")
