import sys
sys.stdin = open('input.txt')

pattern = {
    0:'001101',
    1:'010011',
    2:'111011',
    3:'110001',
    4:'100011',
    5:'110111',
    6:'001011',
    7:'111101',
    8:'011001',
    9:'101111'
}

for i in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    code = ['0' * n]
    flag = True
    for i in range(n):
        temp = input()
        if flag and code != temp:
            code = temp
            flag = False


    i = 0
    decode = []
    while i < m:
        k = 0
        j = 0
        while k < 6 and j < 10 and i + 5 < m:
            if code[i+k] == pattern[j][k]:
                k += 1
            else:
                k = 0
                j += 1

            if k == 6:
                decode.append(j)
                break

        if k == 6:
            i += 6
        else:
            i += 1

    print(*decode)
