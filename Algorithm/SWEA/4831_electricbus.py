'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

[입력]
 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 
[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''

def electric_bus(k, n, m, charger_idxs):

    # charger의 배치가 올바른지 확인
    # 초기 위치에서 범위 내에 충전소가 있는지와 마지막 충전소에서 종점갈 수 있는지
    if charger_idxs[0] > k or charger_idxs[-1] + k < n:
        return 0
    # 충전소마다 간격은 범위내에 이동할 수 있는 간격인지
    for i in range(m-1):
        if charger_idxs[i+1] > charger_idxs[i] + k:
            return 0

    # charger 배치가 올바른 경우
    # 인덱싱하기 위해서 정거장 리스트와 인덱스 맞추기
    charger_arr = [False for _ in range(n+1)]
    for idx in charger_idxs:
        charger_arr[idx] = True # 0 ~ N의 arr에 충전소 위치 저장(True)

    cnt = 0
    i = 0

    while i + k < n: # 종점에 도착할 때 까지
        for j in range(k, 0, -1): # 이동가능한 범위내에 있는 충전소에서 가장 먼 곳부터
            if charger_arr[i + j]: # 충전소가 있다면
                i += j # 다음 인덱스 만들기
                cnt += 1 # 충전 횟수 + 1
                break
    return cnt

if __name__=="__main__":

    T = int(input())

    for test_case in range(1, T + 1):
        # 한번에 이동가능한 정류장 수, 정류장 수, 충전기 갯수
        k, n, m = map(int, input().split())
        charger_idxs = list(map(int, input().split()))
        print(f'#{test_case} {electric_bus(k, n, m, charger_idxs)}')
