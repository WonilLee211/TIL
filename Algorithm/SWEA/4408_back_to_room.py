
def back_to_room(room_info, N):
    # 복도를 2의 배수로 400까지 키로 갖는 딕셔너리 형태로 저장
    corridor = {i: 0 for i in range(2, 402, 2)}

    # 입력된 룸정보 전처리
    # move가 홀수일 경우 짝수로 만들기
    # edge case : 400, 1처럼 move[0]이 move[1]보다 더  큰 경우 정렬해주기
    for move in room_info:
        # 정렬
        if move[0] > move[1]:
            move[0], move[1] = move[1], move[0]

        # 짝수로 만들기
        for i in range(2):
            if move[i] % 2:
                move[i] += 1

        # 복도에 학생별로 지나가는 위치 표시
        for j in range(move[0], move[1] + 1, 2):
            corridor[j] += 1

    # 누적 값 최대가 time
    max_cnt = 0
    for value in corridor.values():
        if value > max_cnt:
            max_cnt = value

    return max_cnt

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        room_info = []

        for i in range(N):
            room_info.append(list(map(int, input().split())))

        print(f'#{tc} {back_to_room(room_info, N)}')