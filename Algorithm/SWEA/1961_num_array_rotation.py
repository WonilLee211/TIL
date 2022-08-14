
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    matrix = [list(map(str, input().split())) for i in range(n)]

    arr = list('' for i in range(n * 3))

    for c1 in range(n):
        for r1 in range(n):
            arr[c1 * 3] += matrix[-1 - r1][c1]
    # arr = ['741', '', '', '852', '', '', '963', '', '']

    for r2 in range(n):
        temp = ''
        for c2 in range(n):
            arr[r2 * 3 + 1] += matrix[-1 - r2][-1 - c2]
    # arr = ['741', '987', '', '852', '654', '', '963', '321', '']

    for c3 in range(n):
        temp = ''
        for r3 in range(n):
            arr[c3 * 3 + 2] += matrix[r3][-1 - c3]
    # arr = ['741', '987', '369', '852', '654', '258', '963', '321', '147']

    print(f"#{test_case}")
    for i in range(n * 3):
        if i % 3 == 2:
            print(arr[i])
        else:
            print(arr[i], end=' ')