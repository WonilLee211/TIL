def pre_process(pattern):
    skip_table = dict()
    M = len(pattern)

    for i in range(M-1):
        skip_table[pattern[i]] = M - 1 - i

    return skip_table

# 패턴이 몇번 중복되는지 반환하는 함수
def boyer_moore(text, pattern):

    skip_table = pre_process(pattern)
    N = len(text)
    M = len(pattern)

    i = 0
    cnt = 0
    while i <= N - M:
        j = M - 1
        k = i + M - 1

        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1

        if j == -1: #일치할 때
            cnt += 1 # 세고
            i += M # 텍스트의 비교 시작점을 M만큼 점프

        else:
            i += skip_table.get(text[i + M - 1], M)

    return cnt

# 카운트 값을 바탕으로 최소 타이핑 횟수 구하는 함수
def min_typing(text, pattern):
    cnt = boyer_moore(text, pattern)
    pt_length = len(pattern)
    # 최소 타이핑 횟수 구하는 수식
    min_type = len(text) - (pt_length - 1) * cnt

    return min_type

if __name__ == '__main__':
    T = int(input())

    for tc in range(1, T + 1):
        text, pattern = input().split()
        result = min_typing(text, pattern)

        print(f'#{tc} {result}')