
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    space = [list(map(int, input().split())) for i in range(n)]

    num_kill = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            kill = 0
            for k in range(m):
                kill += sum(space[i + k][j:j + m])
            num_kill.append(kill)

    max_i = 0
    for i in range(len(num_kill)):
        if num_kill[i] > num_kill[max_i]:
            max_i = i

    print(f"#{test_case}", num_kill[max_i])