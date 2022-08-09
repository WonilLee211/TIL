'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하는 프로그램

[입력]
첫 줄 : 테스트 케이스의 수 T ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄 : 양수의 개수 N( 5 ≤ N ≤ 1000 )
다음 줄 : N개의 양수 ai ( 1 ≤ ai≤ 1000000 )

[출력]
"#T 답"
'''

def min_max(numbers, N):
    # 변수 초기화
    min_idx = 0
    max_idx = 0
    i = 0

    # 값이 가장 큰 값의 인덱스와 가장 작은 값의 인덱스 구하기
    while i < N:
        if numbers[i] > numbers[max_idx]:
            max_idx = i

        if numbers[i] < numbers[min_idx]:
            min_idx = i

        i += 1 # 0 ~ N-1까지 반복

    diff = numbers[max_idx] - numbers[min_idx]

    return diff

if __name__=="__main__":
    T = int(input())
    for test_case in range(1, T +1):
        N = int(input())
        numbers = list(map(int, input().split()))
        print(f'#{test_case} {min_max(numbers, N)}')