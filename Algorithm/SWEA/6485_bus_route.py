'''
버스 정류장 : 1에서 5,000까지 번호가 붙어 있음
버스 노선 : N개
i번째 버스 노선 : 번호가 Ai이상이고, Bi이하인 모든 정류장만을 다니는 버스 노선
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램

[입력]
첫 번째 줄 : 테스트 케이스의 수 T
각 테스트 케이스의 첫 번째 줄 : 하나의 정수 N
다음 N개의 줄의 i번째 줄 : 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )
다음 줄 : 하나의 정수 P ( 1 ≤ P ≤ 500 )
다음 P개의 줄의 j번째 줄 : 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 )

[출력]
'#x 한 줄에 P개의 정수'
j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수
'''

def bus_route(N, route_case, P, C_arr):
    # 0 ~ 5000 인덱스를 가지는 빈 배열
    temp_C = [0 for _ in range(5001)]

    # 입력받은 노선의 A_i, B_i범위에서 버스가 지나는 정류장에 카운팅
    for A_i, B_i in route_case:
        for i in range(A_i, B_i + 1):
            temp_C[i] += 1
        # 확인하고 싶은 정류장 번호에 대해서 Temp_C에서 읽어와서 출력형태 만들기
    result = ''
    for stop in C_arr:
        result += f'{temp_C[stop]}' + ' '

    return result[:-1]

if __name__ == "__main__":

    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())

        route_case = []

        for i in range(N):
            A_i, B_i = map(int, input().split())
            # [(A1, B1), (A2, B2)] 버스 노선 정보
            route_case.append((A_i, B_i))

        P = int(input())
        # [1, 2, 3, 4, 5] 확인하고 싶은 버스 번호
        C_arr = [int(input()) for _ in range(P)]

        print(f'#{test_case} {bus_route(N, route_case, P, C_arr)}')