def pre_process(pattern):
    skip_table = dict()
    M = len(pattern)

    for i in range(M-1):
        skip_table[pattern[i]] = M - 1 - i

    return skip_table

def boyer_moore(text, pattern):

    skip_table = pre_process(pattern)
    N = len(text)
    M = len(pattern)

    i = 0
    while i <= N - M:
        j = M - 1
        k = i + M - 1

        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1

        if j == -1:
            return 1

        else:
            i += skip_table.get(text[i + M - 1], M)

    return 0


if __name__ == '__main__':
    T = int(input())

    for tc in range(1, T + 1):
        pattern = input()
        text = input()
        print(f'#{tc} {boyer_moore(text, pattern)}')