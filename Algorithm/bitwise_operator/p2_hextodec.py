
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

    for i in range(m//7 + 1):
        ans.append(int(temp[i*7:(i+1)*7], 2))
    print(*ans)