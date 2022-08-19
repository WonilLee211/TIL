import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())

    # 스택을 사용해서 교착상태인 경우만 저장하기


    matrix = [input().split() for _ in range(N)]
    # 1 : N, 2 : S
    # maxtrix 윗쪽 : N, maxtrix 아래쪽: S

    stack = [[] for i in range(100)]


    for i in range(100):
        for j in range(100):
            if matrix[j][i] == '1': # N이면 항상 쌓기
                stack[i].append('1')
            # 스택이 비어있지 않을 때만( N이 하나라도 있는 경우)
            # S 쌓기
            elif len(stack) != 0 and matrix[j][i] == '2':
                stack[i].append('2')

    for i in range(100): # 스택의 가장 아래 쪽에 N이 쌓여 있는 경우 없애기
        while len(stack[i]) != 0 and stack[i][-1] == '1':
            stack[i].pop()


    stag_cnt = 0 # NS 패턴 매칭(brute_force)
    for i in range(100):
        idx = 0
        while idx + 1 < len(stack[i]):
            if stack[i][idx] + stack[i][idx+1] == '12':
                stag_cnt += 1
            idx += 1

    print(f'#{tc} {stag_cnt}')