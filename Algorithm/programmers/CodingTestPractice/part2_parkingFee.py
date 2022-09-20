import math
def solution(fees, records):
    '''
    [["05:34","5961","IN"],
    ["06:00","0000","IN"],
    ["06:34","0000","OUT"],
    ["07:59","5961","OUT"],
    ["07:59","0148","IN"],
    ["18:59","0000","IN"],
    ["19:09","0148","OUT"],
    ["22:59","5961","IN"],
    ["23:00","5961","OUT"]]
    '''
    c_nums = []
    for i in range(len(records)):
        records[i] = records[i].split()
        c_nums.append(records[i][1])
    c_nums = list(set(c_nums))                      # 차 번호 수집

    p_time = {c_num: [] for c_num in c_nums}        # 입출 시간 분으로 바꿔서 저장
    for rcd in records:
        h, m = map(int, rcd[0].split(':'))
        m += h * 60                                 # 분으로 바꿔서 저장하기
        p_time[rcd[1]].append(m)

    for k in p_time.keys():
        if len(p_time[k]) % 2 == 1:
            p_time[k].append(23 * 60 + 59)          # 홀수이면 2359을 분으로 추가

    for k in p_time.keys():                         # 짝맞춰서 시간 계산
        for i in range(0, len(p_time[k]), 2):
            p_time[k][i+1], p_time[k][i] = p_time[k][i+1] - p_time[k][i], 0

    answer = []
    for k in sorted(c_nums):                        # 차번호 순서 맞춰서
        acc = sum(p_time[k])
        fee = fees[1]
        if acc > fees[0]:
            fee += math.ceil((acc - fees[0])/fees[2]) * fees[3] # 올림 주의
        answer.append(fee)

    return answer
