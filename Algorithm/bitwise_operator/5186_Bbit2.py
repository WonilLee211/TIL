import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    Rnum = float(input())

    RBbin = ''
    temp = 0
    for i in range(12):
        bit = round(2 ** -(i + 1), 15)

        if temp + bit <= Rnum:
            RBbin += '1'
            temp += bit
            if temp == Rnum:
                break
        else:
            RBbin += '0'

    print(f'#{tc} ', end='')
    print(RBbin if Rnum == float(temp) else 'overflow')