def dfs(cnt, depth, now_sum, dupli):
    global min_sum

    if cnt == depth:
        if now_sum < min_sum:
            min_sum = now_sum
    elif now_sum >= min_sum: # 이미 최소값보다 크면 멈추기
        return
    else:
        for i in range(N):
            if i not in dupli: # 같은 열 중복 방지
                dupli.append(i)
                dfs(cnt+1, depth, now_sum + data[cnt][i], dupli)
                dupli.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(list(map(int, input().split())) for _ in range(N))

    min_sum = 0
    for i in range(N):
        min_sum += data[i][i]

    dupli = []
    dfs(0, N, 0, dupli)

    print(f'#{tc} {min_sum}')