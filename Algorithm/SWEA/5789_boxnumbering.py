'''
i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램


[입력]
첫 번째 줄 : T
각 테스트 케이스의 첫 번째 줄 : 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분
다음 Q개의 줄의 i번째 줄 : Li, Ri (1 ≤ Li ≤ Ri ≤ N)

[출력]
‘#x (Q개의 작업을 수행한 다음 1번부터 N번까지의 상자에 적혀있는 값)'
'''

def box_numbering(LR_arr):

    box_arr = [0 for _ in range(N+1)] # 인덱스 맞추기 편하게 한칸 더 만들기

    i = 0
    # 범위마다 box_arr에 i 값 저장
    for L, R in LR_arr:
        i += 1
        for idx in range(L, R + 1):
            box_arr[idx] = i

    result = ''
    
    # 인덱스 0은 제외
    for box in box_arr[1:]:
        result += f'{box}' + ' '

    return result[:-1]

if __name__ == "__main__":

    T = int(input())
    for test_case in range(1, T + 1):
        # 이번 문제는 입력을 어떻게 저장하는지가 매우 중요
        N, Q = map(int, input().split())
        LR_arr = []
        
        # Q개의 범위를 튜플 형태로 리스트에 저장
        for _ in range(Q):
            L, R = map(int, input().split())
            LR_arr.append((L, R))

        print(f'#{test_case} {box_numbering(LR_arr)}')
