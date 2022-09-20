for i in range(1, int(input()) + 1):
    hex_input = input()
    n = len(hex_input)
    ans = []
    temp = ''

    for s in hex_input[-1::-1]:
        dec = int('0x' + str(s), 16)
        for i in range(4):
            temp += '1' if dec & (1 << i) else '0'
    temp = temp[-1::-1]

    m = len(temp)
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
        9:'101111'}

    i = 0
    while i < m:
        k = 0
        j = 0
        while k < 6 and j < 10 and i + 5 < m:
            if temp[i+k] == pattern[j][k]:
                k += 1
            else:
                k = 0
                j += 1

            if k == 6:
                ans.append(j)
                break

        if k == 6:
            i += 6
        else:
            i += 1

    print(*ans)
