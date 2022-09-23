import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n = int(input())
    InitT = [0 for i in range(n)]
    EndT = [0 for i in range(n)]

    for i in range(n):
        InitT[i], EndT[i] = map(int, input().split())

    for i in range(n-1):
        MinI = i
        for j in range(i, n):
            if EndT[j] < EndT[MinI]:
                MinI = j
        EndT[i], EndT[MinI] = EndT[MinI], EndT[i]
        InitT[i], InitT[MinI] = InitT[MinI], InitT[i]
    ''' 시작시간과 종료시간 인덱스 맞춰서 정렬
    [4, 8, 17, 20, 23] 
    [14, 18, 20, 23, 24]
    '''
    i = 0
    cnt = 0
    while True:
        t = EndT[i]             # 현재 시간
        j = i + 1
        temp = 1                # j 번째 위치에서마다 카운팅할 변수

        while j < n:            # 마지막 화물작업까지 비교
            if t <= InitT[j]:   # j단계 화물 시작 시간이 현재 끝나는 시간과 같거나 클 때
                t = EndT[j]     # 다음 화물로 선택
                temp += 1       # 카운팅
            j += 1

        if temp > cnt:
            cnt = temp
        i += 1

        if n - i < cnt:         # 탈출 구문/  cnt 초기 값이 0이어서 뒤에 작성
            break               # 현재 카운트 갯수보다 n - i이 작으면 반복할 의미없음
    print(f'#{tc} {cnt}')