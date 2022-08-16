# 행방향 회문 검사 함수
def test_row(str_arr, N, M):
    answer = ''

    for i in range(N):
        # 행의 길이에서 회문길이를 뺀 만큼만 이동 가능
        for j in range(N - M + 1):
            test = str_arr[i][j:j + M]

            if test == test[-1::-1]:
                answer = test
                break

        if answer != '':
            break

    return answer


def palindrome(str_arr, N, M):
    answer = test_row(str_arr, N, M)
    if answer == '':
        str_arr = list(zip(*str_arr))  # 전치행렬 만들기
        # 출력이 튜플로 나오기 때문에 문자열로 만들어주기
        answer = ''.join(test_row(str_arr, N, M))

    return answer


if __name__ == '__main__':
    T = int(input())

    for tc in range(1, T + 1):
        N, M = list(map(int, input().split()))
        str_arr = []
        for i in range(N):
            # 문자열 그대로 받아오기
            str_arr.append(input())

        print(f'#{tc} {palindrome(str_arr, N, M)}')