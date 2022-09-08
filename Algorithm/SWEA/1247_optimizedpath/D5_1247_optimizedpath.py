from itertools import permutations

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    data = list(map(int,input().split()))

    # 리스트 슬라이스를 통해 집과 회사 고객 위치 분리하기
        # 순열 조합 때 튜플 사용할 것이기 때문에 각각 튜플 자료형으로 바꾸기
    home, company = tuple(data[:2]), tuple(data[2:4])
    clients = list( (data[i],data[i+1]) for i in range(4,2*n+3,2))
    
    min_acc = float("inf")  # 최소 거리를 저장할 변수
    
    # 스퀀스 형태는 [(([((70, 40), (30, 10), (10, 5), (90, 70), (50, 20)), ...))]
    for clientpath in permutations(clients):
        # 경로의 경우 중 한가지가 path에 담김
        path = [company, *list(clientpath), home] # 튜플묶음 벗겨내기

        acc = 0

        for i in range(0,len(path)-1):  # path의 경우마다 거리 누적 계산
            acc += abs(path[i][0]-path[i+1][0])+ abs(path[i][1]-path[i+1][1])

        if min_acc > acc:   # 최소 거리 구하기
            min_acc = acc
    
    print(f"#{tc} {min_acc}")

