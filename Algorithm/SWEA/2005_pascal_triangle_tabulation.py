
for tc in range(1, T+1):

    N = int(input())
    arr = [[] for _ in range(N)]

    arr[0].append(1) # arr = [[1] , [1, 1] 2 [1, 2, 1] [1,3, 3, 1]]

    for i in range(1, N):
        arr[i].append(1)

        if i == 1:
            arr[i].append(1)
            continue

        for j in range(1, i):
            arr[i].append(arr[i-1][j-1] + arr[i-1][j])

        arr[i].append(1)

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])