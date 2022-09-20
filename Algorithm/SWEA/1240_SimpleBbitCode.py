pattern = {
    0:'0001101',
    1:'0011001',
    2:'0010011',
    3:'0111101',
    4:'0100011',
    5:'0110001',
    6:'0101111',
    7:'0111011',
    8:'0110111',
    9:'0001011'
}

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    code = '0' * m
    flag = True
    for i in range(n):
        temp = input()
        if flag and code != temp:
            code = temp
            flag = False
    L1 = 0
    for i in range(m-1, -1, -1):
        if code[i] == '1':
            L1 = i
            break

    code = code[L1-55:L1+1]
    decode = []
    for i in range(8):
        for k, v in pattern.items():
            if v == code[i*7:(i+1)*7]:
                decode.append(k)
                break

    total = 0
    for i in range(8):
        total += decode[i] if i % 2 else int(decode[i])*3

    ans = sum(decode) if not total % 10 else 0
    print(f'#{tc} {ans}')

