
'''
주어진 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램
'''

def BruteForce(p, t, M , N, start):
    i, j = start, 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j  # 일치하지 않을 경우,  i는 비교 시작점의 다음 위치
            j = -1  # 패턴 첫자리
        i += 1
        j += 1

    if j == M:
        return i - M  # 검색 성공
    else:
        return -1  # 검색 실패

def count_pattern(pattern, text):

    cnt = 0
    N, M = len(text), len(pattern)
    start = 0
    while start != -1:
        start = BruteForce(pattern, text, M, N, start)

        if start != -1:
            cnt += 1
            start += 1
        else:
            break
    return cnt

if __name__ == '__main__':

    T = 10
    for tc in range(1, T + 1):
        test_case = int(input())
        pattern = input()
        text = input()

        print(f'#{test_case} {count_pattern(pattern, text)}')