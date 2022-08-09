'''
N= 2^a x 3^b x 5^c x 7^d x 11^e
N이 주어질 때 a, b, c, d, e 를 출력


[제약 사항]
N : 2 이상 10,000,000 이하


[입력]
가장 첫 줄 : 테스트 케이스의 개수 T
각 테스트 케이스의 첫 번째 줄 : N

[출력]
'#t 정답'
'''

def factor_into_primes(number):
    # 나눌 값 리스트와 지수 저장 리스트 만들기
    primes = [2, 3, 5, 7, 11]
    factors_arr = [0 for _ in range(12)]

    # 프라임마다 나머지가 나올 때까지 나누고 factor_arr에 나누기 횟수 저장
    for prime in primes:
        while not number % prime:
            number //= prime
            factors_arr[prime] += 1

    # 결과값 문자열 형태로 반환
    result = ''
    for prime in primes:
        result += f'{factors_arr[prime]}' + ' '

    # 오른쪽 끝 부분 공백빼고 출력
    return result[:-1]

if __name__=="__main__":

    T = int(input())
    for test_case in range(1, T + 1):

        number = int(input())
        print(f'#{test_case} {factor_into_primes(number)}')

