def solution(fees, records):
    status = ['IN', 'OUT']
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
    c_nums = list(set(c_nums))

    p_time = {c_num: [] for c_num in c_nums}
    for rcd in records:
        h, m = map(int, rcd[0].split(':'))
        m += h * 60
        p_time[rcd[1]].append(m)

    answer = []
    return records