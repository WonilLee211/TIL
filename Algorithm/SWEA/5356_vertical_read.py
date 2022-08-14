
from collections import deque

def vertical_read(rows):

    str_col = ''

    # 모든 행의 문자들이 없어질 때까지
    while rows[0] or rows[1] or rows[2] or rows[3] or rows[4]:
        # 행을 돌면서 요소가 있다면 popleft()
        for i in range(5):
            if rows[i]:
                str_col += rows[i].popleft()

    return str_col

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        rows = [deque(list(input())) for _ in range(5)]
        print(f'#{tc} {vertical_read(rows)}')