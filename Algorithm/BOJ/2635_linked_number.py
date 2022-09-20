import sys
sys.stdin = open('input.txt')

def recursive(num, next, cnt, arr):
    arr.append(next)
    cnt += 1

    if next > num:
        return cnt, arr

    return recursive(next, num - next, cnt, arr)

def max_cnt(num):

    max_cnt_ = 0
    max_arr_ = 0

    for i in range(1, num):
        arr = [num]
        cnt, arr = recursive(num, i, 1, [num])

        if cnt > max_cnt_:
            max_cnt_ = cnt
            max_arr_ = arr

    return max_cnt_, max_arr_

if __name__ == '__main__':
    num = int(input())
    if num == 1:
        result = 4, [1, 1, 0, 1]
    else:
        result = max_cnt(num)

    print(result[0])
    print(*result[1])