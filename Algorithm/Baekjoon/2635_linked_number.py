import sys
sys.stdin = open('input.txt')

def recursive(num, next, cnt):
    arr.append(next)
    cnt += 1

    if next > num:
        return cnt

    return recursive(next, num - next, cnt)

def max_cnt(num):

    max_cnt_ = 0
    max_arr_ = 0

    for i in range(1, num):
        arr = [num]
        cnt = recursive(num, i, 1)

        if cnt > max_cnt_:
            max_cnt_ = cnt
            max_arr_ = arr

    return max_cnt_, max_arr_

if __name__ == '__main__':
    num = int(input())
    global arr

    arr = [num]

    result = max_cnt(num)
    print(result[0])
    print(*result[1])