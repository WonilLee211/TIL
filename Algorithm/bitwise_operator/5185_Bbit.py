import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n, bit = input().split()

    bin = ''
    for i in range(int(n)):
        dec_i = int(bit[i], 16)
        temp = ''
        for j in range(4):
            temp = ('1' if dec_i&(1<<j) else '0') + temp

        bin += temp

    print(f'#{tc} {bin}')