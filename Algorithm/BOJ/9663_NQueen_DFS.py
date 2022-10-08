def dfs(d):
    global cnt
    if d == n:
        cnt += 1
        return
    else:
        for i in range(n):
            flag = True
            case[d] = i
            # 현재 행의 이전 행들과 비교
            for j in range(d):
                # 열방향이 같거나 대각선일 경우
                if case[j] == case[d] or abs(case[d] - case[j]) == abs(d - j):
                    flag = False
                    break

            if flag:
                dfs(d + 1)

n = int(input())
case = [0 for i in range(n)]
cnt = 0
dfs(0)
print(cnt)