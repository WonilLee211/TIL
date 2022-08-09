'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램
[입력]
첫 줄 : 테스트 케이스 개수 T ( 1 ≤ T ≤ 50 )
테스트케이스의 첫 줄 : 정수의 개수 N과 구간의 개수 M ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄 : N개의 정수 ai ( 1 ≤ a ≤ 10000 )

[출력]
"#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

def sumofintervals(numbers, N, M):

    sum_arr = [0 for _ in range(N - M + 1)] # 범위는 총 길이 - 부분합 길이 + 1

    for i in range(N - M + 1): # 부분 합 계산하기
        for j in range(M):
            sum_arr[i] += numbers[i + j]

    max_idx = 0
    min_idx = 0
    for i in range(1, N - M + 1): # 최소값 최대값 인덱스 구하기
        if sum_arr[i] > sum_arr[max_idx]:
            max_idx = i

        if sum_arr[i] < sum_arr[min_idx]:
            min_idx = i

    diff = sum_arr[max_idx] - sum_arr[min_idx]

    return diff

if __name__=="__main__":

    T = int(input())
    for test_case in range(1, T +1):

        N, M = map(int, input().split())
        numbers = list(map(int, input().split()))

        print(f'#{test_case} {sumofintervals(numbers, N, M)}')
