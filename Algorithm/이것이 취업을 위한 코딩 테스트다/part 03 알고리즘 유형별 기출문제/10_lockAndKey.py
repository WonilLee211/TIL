import sys
sys.stdin = open('input.txt')

'''
n = 격자 가로세로
m = 키 가로세로

자물쇠를 열 수 있는지 없는지 여부
0은 홈부분
1은 돌기부분
열쇠의 돌기와 자물쇠의 홈이 일치해야 함
열쇠의 돌기와 자물쇠의 돌기가 만나면 안됨

락에 홈은 모두 채워져야 함.

'''
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
n = len(lock)
m = len(key)

min_i, min_j = n, n
cnt_zero = 0
for i in range(n):
    for j in range(n):
        if lock[i][j] == 0:
            min_i, min_j = min(i, min_i), min(j, min_j)
            cnt_zero += 1

def rotation(arr):
    k = len(arr)
    temp = list([0] * k for i in range(k))

    for i in range(k):
        for j in range(k):
            temp[j][-i - 1] = arr[i][j]
    # print(temp)
    return temp

cnt_rotate = 0
ans = False

while cnt_rotate < 4:

    for i in range(n):
        for j in range(n): # 락의 모든 점에 대해서

            if i > min_i or j > min_j: # 락에 홈들의 가장 작은 인덱스보다 커지면 break
                break

            cnt = 0
            flag = False

            for x in range(m):

                sub_key = [0 for i in range(x + 1)]

                for y in range(x + 1):
                    # print(x)
                    sub_key[y] = key[m - 1 - x + y][m - 1 - x:]

                for r in range(x + 1):
                    flag2 = False
                    for c in range(x + 1):
                        if i + r >= n or j + c >= n:
                            continue

                        if lock[i + r][j + c] + key[r][c] == 1:
                            if key[r][c]:
                                cnt += 1
                        else:
                            flag2 = True
                            break
                    if flag2:
                        break

                # print('a', flag2)
                if not flag2 and cnt == cnt_zero:
                    flag = True
                    ans = True
                    break

            if flag:
                break
        if flag:
            break
    if not flag:
        temp = rotation(key)
        key = [temp[i] for i in range(n)]
        cnt_rotate += 1
    else:
        break

print(ans)
