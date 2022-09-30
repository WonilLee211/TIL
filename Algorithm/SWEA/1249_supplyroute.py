from collections import deque
#방향 경우의 수
direction = [(1,0), (0,1), (-1,0), (0,-1)]

T = int(input())
for tc in range(1,T+1):

    N = int(input())

    #map 정보 저장 ** 여기서 인풋값 사이에 띄어쓰기가 없기 때문에 인풋을 바로 리스트화하기 
    MapInfo = list(list(map(int, list(input()))) for _ in range(N))
    
    # 위치마다 최소거리 저장하기 
    MapDistAcc = list(list(float('inf') for _ in range(N)) for _ in range(N))

    MapDistAcc[0][0] = 0

    queue = deque()
    queue.append((0,0))
    
    while len(queue):       ## queue가 빌 때까지
        y, x = queue.popleft()      ## queue의 왼쪽부터(deque는 왼쪽부터 꺼낼 떄 시간복잡도가 O(1), 뒤에서 꺼낼 때 O(n) )

        for r, c in direction:      ## 해당 위치에서 이동방향마다,
            NewY, NewX = y+r, x+c

            if 0 <= NewY <= N-1 and 0 <= NewX <= N-1:     ## 이동하는 위치가 제한된 인덱스 안에 있고,

                ## 각 위치마다의 누적값들보다 작다면,
                if MapDistAcc[NewY][NewX]> MapDistAcc[y][x] + MapInfo[NewY][NewX]:
                    ## 위치의 누적값을 업데이트하고,
                    MapDistAcc[NewY][NewX] = MapDistAcc[y][x] + MapInfo[NewY][NewX]
                    ## queue에 업데이트된 위치의 인덱스를 추가해준다.
                    queue.append((NewY,NewX))

    print(f"#{tc} {MapDistAcc[N-1][N-1]}")