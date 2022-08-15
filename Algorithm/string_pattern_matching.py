'''
def bruteforce(pattern, text):

    N = len(text)
    M = len(pattern)

    for i in range(N - M + 1):
        for j in range(M):
            if text[i] != pattern[j]: # 불일치하면 다음 i로 이동
                break
            i += 1 # text[i] = pattern[j]인 상황에서 i + 1로 업데이트

        else: # 패턴 전체와 매칭된 위치
            return i -j
    else:
        return -1

'''
''' bruteforce_while문으로 구현
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
'''
'''KMP
pattern = 'abcdabce'
def pre_process(pattern):
    M = len(pattern)
    lps = [0 for _ in range(M)]
    j = 0
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
        # 같은 문자라면 다음 문자 비교
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M: # 패턴이 전부 일치할 때
            return i - M # text의 위치
    return -1
'''
'''보이어 무어 알고리즘
def pre_process(pattern):

    M = len(pattern)
    skip_table = {}

    for i in range(M-1):
        skip_table[pattern[i]] = M - 1 - i

    return skip_table

def boyer_moore(text, pattern):
    skip_table = pre_process(pattern)
    N, M = len(text), len(pattern)

    i = 0
    while i <= len(text) - M:
        j = M - 1   # 뒤에서 비교해야 되기 때문 j를 끝에 index
        k = i + (M-1)  # 비교를 시작할 위치 (현재위치 + M번째 인덱스)

        # 비교할 j가 남아있고, text와 pattern이 일치하면
        # 그 다음 앞에 글자를 비교하기 위해 인덱스 감소
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1
        if j == -1:
            return i
        else: # 일치하지 않는 경우
            # 패턴 스킵할 위치 찾기. 텍스트 비교 시작 위치 문자와 일치하는 패턴 문자까지 당기기.
            # key가 없는 경우 : 패턴의 맨끝 자리나 문자 중 키로 가지고 있지 않는 경우
                # 패턴 전체를 당긴다.
            i = skip_table.get(text[i + (M -1)], M)

    return -1
'''