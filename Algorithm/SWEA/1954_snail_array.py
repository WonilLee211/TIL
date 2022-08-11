from collections import deque

T = int(input())
for test_case in range(1, T + 1):

    n = int(input())
    temp = [i for i in range(1, n**2 + 1)]

    # deque 자료형 사용
    ordered_arr = deque(temp)

    i = 0 # i : 정렬방향을 결정할 변수
    idx = [0, 0] # 값이 저장이 위치를 저장

    if n % 2:    # 값이 저장될 마지막 위치
        last_idx = [n//2, n//2]
    else:
        last_idx = [n//2 , n//2 - 1]

    # 달팽이 배열을 저장할 2차원 리스트
    result = list([0]*n for _ in range(n))
    result[0][0] = ordered_arr.popleft()

    while idx != last_idx:    # idx가 마지막 저장 위치가 될 때 까지
        if i == 0: # 오른쪽으로 나아가는 경우
            # 열이 범위를 벗어나지 않고 다음 값을 저장할 위치가 result가 비어있을 경우
            while idx[1] < n-1 and not result[idx[0]][idx[1]+1]:
                res = ordered_arr.popleft() # 왼쪽 값을 빼내서 작은 값이 순서대로 나오도록 설정
                idx[1] += 1
                result[idx[0]][idx[1]] = res

        if i == 1: # 아래로 나아가는 경우
            while idx[0] < n-1 and not result[idx[0]+1][idx[1]]:
                res = ordered_arr.popleft()
                idx[0] += 1
                result[idx[0]][idx[1]] = res

        if i == 2: # 왼쪽으로 나아가는 경우
            while idx[1] > 0 and not result[idx[0]][idx[1]-1]:
                res = ordered_arr.popleft()
                idx[1] -= 1
                result[idx[0]][idx[1]] = res

        if i == 3: # 위쪽으로 나아가는 경우
            # 위쪽으로 나아갈 땐 범위를 벗어날 가능성 없음
            while not result[idx[0]-1][idx[1]]:
                res = ordered_arr.popleft()
                idx[0] -= 1
                result[idx[0]][idx[1]] = res

        # n 값이 커져서 회전 수가 많아지더라도 방향의 조건을 0~3 순서로 돌 수 있도록 설정
        i += 1
        i %= 4

    print(f"#{test_case}")
    for r in range(n):
        for c in range(n):
            print(result[r][c], end=" ")
        print()