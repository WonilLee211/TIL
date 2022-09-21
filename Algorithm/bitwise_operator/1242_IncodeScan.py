import sys
sys.stdin = open('input.txt')

decoding = {
    '0001101':0, '0011001':1, '0010011':2, '0111101':3,'0100011':4,
    '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9
}

def hextobin(r):
    row = ''
    for s in r:
        temp = ''
        dec_s = int(s, 16)
        for j in range(4):
            temp = ('1' if dec_s & (1 << j) else '0') + temp
        row += temp
    return row

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    pass_row = '0' * m
    code_arr = []
    ans = []
    decodes = []
    data = [input().rstrip() for i in range(n)]
    found = []

    for row in data:
        if row != pass_row and row not in code_arr:
            code_arr.append(row)

    for row in code_arr:
        Bbin = hextobin(row)

        j = len(Bbin) - 1
        while j > 56:
            for k in range(j, 55, -1):
                if Bbin[k] != '0':
                    j = k
                    break
            else:
                break


            cnt = 0
            ratio = 1
            min_r = 2000
            for k in range(j, 0, -1):
                if Bbin[k] == Bbin[k-1]:
                    ratio += 1
                elif cnt == 3:
                    break
                else:
                    cnt += 1
                    if min_r > ratio:
                        min_r = ratio
                    ratio = 1


            cnt1 = 1
            code = Bbin[j]
            while cnt1 < 56:
                cnt1 += 1
                j -= min_r
                code = Bbin[j] + code

            if code not in ans:
                ans.append(code)

                # decode_n = []
                # for i in range(8):
                #     if code[i * 7:i * 7 + 7] in decoding.keys():
                #         decode_n.append(decoding[code[i * 7:i * 7 + 7]])
                #     else:
                #         decode_n = []
                #         break

    answer = 0
    for j in range(len(ans)):
        code = ans[j]
        decode_n = []
        for i in range(8):
            decode_n.append(decoding[code[i * 7:i * 7 + 7]])

        total = 0
        for w in range(8):
            total += decode_n[w] if w % 2 else decode_n[w] * 3
        answer += sum(decode_n) if not total % 10 else 0
    print(f'#{tc} {answer}')
