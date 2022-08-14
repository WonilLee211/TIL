
def cut_stick(data):
    cnt = 0
    stick = 0

    for i in range(len(data)-1):
        # 레이저가 만들어지는 경우
        if data[i] == '(' and data[i+1] == ')':
            cnt += stick
        # 막대가 생성되는 경우
        if data[i] == '(' and data[i+1] != ')':
            stick += 1
        # 막대가 닫혀서 잘리는 경우
        if data[i] != '(' and data[i+1] == ')':
            cnt += 1
            stick -= 1

    return cnt

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        data = input()
        print(f'#{tc} {cut_stick(data)}')

'''
문자 패턴 매칭 알고리즘 

시간초과

입력받고
레이저 위치 구하기
레이저 괄호 지우기

괄호마다 포함하고 있는 레이저 수 + 1이 잘린 막대기 갯수
    ")" 위치 인덱스 구하기
    가장 가까운 "("의 인덱스 구해서 범위 구하기
    범위 내에 레이저수 구하기
    counting
'''
'''
def pre_process(pattern):
    M = len(pattern)
    skip_table = dict()

    for i in range(M -1):
        skip_table[pattern[i]] = M - 1 - i

    return skip_table

def boyer_moore(text, pattern, start):
    N, M = len(text), len(pattern)
    skip_table = pre_process(pattern)

    i = start
    while i <= N - M:
        j = M - 1
        k = i + (M - 1)

        while j != -1 and pattern[j] == text[k]:
            j -= 1
            k -= 1

        if j == -1:
            return i
        else:
            i += skip_table.get(text[i+M-1], M)

    return -1

def cut_stick(data):

    data_arr = list(data)

    # 레이저 인덱스 정보 받기
    laser_idxs = []
    start = 0

    while True:
        start = boyer_moore(data, '()', start)
        if start != -1:
            laser_idxs.append(start)
            start += 2
        else:
            break

    for i in laser_idxs:
        data_arr[i], data_arr[i+1] = 0, 0

    # ")" 위치 구하기
    close_idxs = []
    start = 0

    while True:
        start = boyer_moore(data_arr, ')', start)
        if start != -1:
            close_idxs.append(start)
            start += 1
        else:
            break

    cnt = 0

    for right in close_idxs:

        for i in range(right, -1, -1):
            if data_arr[i] =='(':
                left = i

        # 컷팅 갯수 구하기
        for laser in laser_idxs:
            if left < laser < right:
                cnt += 1
        cnt += 1

        # 갯수 센 막대기 지우기
        data_arr[left], data_arr[right] = 0, 0

    return cnt

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        data = input()
        print(f'#{tc} {cut_stick(data)}')
'''