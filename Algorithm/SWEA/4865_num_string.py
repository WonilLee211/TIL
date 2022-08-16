# 문자가 text에 얼마나 많이 중복되는지 세는 함수
def frequency(text, alpha):
    cnt = 0

    for x in text:
        if x == alpha:
            cnt += 1

    return cnt

# 행별로 max_cnt 구하는 함수
def cnt_alphabet(text, pattern):
    max_cnt = 0

    for alpha in pattern:
        cnt = frequency(text, alpha)
        if cnt > max_cnt:
            max_cnt = cnt

    return max_cnt



if __name__ == '__main__':
    T = int(input())

    for tc in range(1, T + 1):
        pattern = input()
        text = input()
        print(f'#{tc} {cnt_alphabet(text, pattern)}')