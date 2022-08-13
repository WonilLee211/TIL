def bruteforce(pattern, text):

    N = len(text)
    M = len(pattern)

    for i in range(N - M + 1):
        for j in range(M):
            if text[i] != pattern[j]: # 불일치하면 다음 i로 이동
                break
            i += 1 # text[i] = pattern[j]인 상황에서 i + 1로 업데이트

        else: # 패턴 전체와 매칭된 위치
            return i
    else:
        return -1

def bruteforce1(pattern, text):

    N = len(text)
    M = len(pattern) #
    i, j = 0, 0 # 텍스트 인덱스, 패턴 인덱스

    while i < N and j < M:
        if text[i] != pattern[j]:
            i, j = i - j, -1
        i, j = i + 1, j + 1

    if j == M: # 패턴이 매칭된 경우,
        return i - j

    return -1

def pre_process(pattern):
    M = len(pattern)
    lps = [0 for _ in range(M)]

    for i in range(1, M):
        if pattern[i] == pattern[j]: # 같으면 lps에 중복된 횟수 + 1을 저장
            lps[i] = j + 1
            j += 1

        else:
            j = 0
            if pattern[i] == pattern[j]: # edge case : pattern이 'aa'같은 경우
                lps[i] = j + 1
                j += 1

    return lps

def KMP(pattern, text):

    lps = pre_process(pattern)
    N, M, i, j = len(text), len(pattern), 0, 0

    while i < N and j < M:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            return i - M
    return -1

