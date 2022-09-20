import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    flag = False

    i = 0

    while True:
        i += 1

        if i ** 3 == n:
            print(f'#{tc} {i}')
            break
        elif i ** 3 > n:
            flag = True
            break

    if flag:
        print(f'#{tc} -1')
