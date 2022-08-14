'''
주어진 영어 문장에서 문자열 정렬하기
boyer_moore 적용
'''
def pre_process(pattern):
    M = len(pattern)  # 패턴의 길이

    skip_table = dict()
    for i in range(M - 1):
        skip_table[pattern[i]] = M - i - 1

    return skip_table

def boyer_moore(text, pattern, start):
    skip_table = pre_process(pattern)
    m = len(pattern)

    i = start # text index
    while i <= len(text) - m :   #패턴 글자 전까지만 비교하면 됨
        j = m - 1 #뒤에서 비교해야 되기 때문 j를 끝에 index로 설정
        k = i + (m-1) #비교를 시작할 위치 (현재위치 + m번째 인덱스)
        #비교할 j가 남아있고 text와 pattern이 일치하면 그 다음 앞에 글자를 비교하기 위해 인덱스 감소
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1
        if j == -1: # 일치함
            return i
        #일치하지 않는다면
        else:
            # i를 비교할 시작 위치를 skip table에서 가져온다.
            i += skip_table.get(text[i+m-1], m)
    return -1 #일치하는 패턴 없음

def planet_sort(num_list, text):
    result = ''
    for pattern in num_list:
        start = 0
        while start != -1:
            start = boyer_moore(text, pattern, start)

            if start != -1:
                result += pattern + ' '
                start += 1
            else:
                break

    return result

if __name__ == '__main__':

    T = int(input())
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for tc in range(1, T + 1):
        N = int(input()[3:])
        text = input()

        print(f'#{tc} {planet_sort(num_list, text)}')