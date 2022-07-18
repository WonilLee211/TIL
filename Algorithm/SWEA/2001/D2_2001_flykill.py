'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!
[제약 사항]

1. N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

다음 N 줄에 걸쳐 N x N 배열이 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    space = [list(map(int, input().split())) for i in range(n)]
    
    num_kill = []
    for i in range(n-m+1): # 파리채가 y방향으로 이동할 수 있는 거리만큼
        for j in range(n-m+1): # 파리채가 x방향으로 이동할수 있는 만큼
            kill = 0 # 킬 누적값 초기화
            for k in range(m): # 파리채 크기 만큼 y방향으로 이동
                kill += sum(space[i+k][j:j+m]) # 리스트 행마다 x방향으로 값 합치기
            num_kill.append(kill) # 포인트마다 기록 저장
            
            
    print(f"#{test_case}", max(num_kill))
