# 행방향 회문 검사 함수
def test_row(text):

    if text == text[-1::-1]:
        return len(text)

    else:
        return 0

# 행을 돌면서 가장 긴 회문 찾는 함수
def palindrome2(str_arr):

    longest = 0
    for i in range(100):
        row = str_arr[i] # 0 ~ 99까지 행
        j = 99 #후단
        k = 0 # 전단
        while j > k:
            if row[k] == row[j]: # 앞과 끝이 같다면 회문 검사
                length = test_row(row[k:j + 1])

                if length > longest: # 회문 길이가 가장 길다면 저장
                    longest = length

            j -= 1 # k값을 줄이면서 다음 회문 찾기
            # j가 줄면서 k와 같아지고 현재 가장 긴 회문 길이보다 범위가 남는다면
            if j == k or 99 - k + 1 > longest:
                k += 1 # k 증가시켜서 다음 회문 찾기
                j = 99 # j는 초기화

    return longest

# 행과 열을 비교하는 함수
def longest_palindromr2(str_arr):
    row_longest = palindrome2(str_arr)
    col_longest = palindrome2(list(zip(*str_arr)))

    return row_longest if row_longest > col_longest else col_longest

if __name__ == '__main__':

    for tc in range(1, 11):

        str_arr = []
        n = int(input())

        for i in range(100):
            str_arr.append(input())

        print(f'#{tc} {longest_palindromr2(str_arr)}')

