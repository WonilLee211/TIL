import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input()) + 1):
    b = input()
    tri = input()
    trans_b = ['1', '0']
    trans_t = [['1', '2'], ['0', '2'], ['1', '0']]

    for i in range(len(b)):
        ans = ''
        pred_b = b[:i] + trans_b[int(b[i])] + b[i+1:]
        for j in range(len(tri)):
            for k in range(2):
                pred_t = tri[:j] + trans_t[int(tri[j])][k] + tri[j + 1:]


                if int(pred_t, 3) == int(pred_b, 2):
                    ans = int(pred_t, 3)

                    break
        if ans:
            break
    print(f'#{tc} {ans}')
