import sys
sys.stdin = open('input.txt')

n = int(input())

# 피보나치 행렬 제곱 공식 사용
# 논리
# 피보나치를 행렬의 제곱으로 구한다.
#  제곱의 결과를 제곱한다. ((2**2)**2) ... >> 모든 자연수 n은 2의 제곱 수로 구할 수 있기 때문
# n = 100이라면, 64 + 32 + 4
# 이러면 O(lgn)으로 시간 복잡도를 줄일 수 있다.

''' 피보나치 수의 행렬화
[[F(n + 1), F(n)],  [[1, 1],
 [F(n), F(n-1)]]     [1, 0]]
'''

def matrix_mul(a, b):
    new = list([0] * 2 for _ in range(2))
    '''
    11 11
    10 10
    '''
    # 행렬의 곱
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j] += a[i][k] * b[k][j]
            new[i][j] %= 1000000007
    return new

def get_nth(n):
    k = 0
    # 답 저장 위치
    ones = [[1, 0], [0, 1]]
    f_mat = [[1, 1], [1, 0]]

    while 2**k <= n:            # 모든 자연수는 2의 제곱 수의 합으로 표현할 수 있다.
        if n & (1 << k):        # n = 100이라면, 64 + 32 + 4
            ones = matrix_mul(ones, f_mat)
        k += 1
        f_mat = matrix_mul(f_mat, f_mat)    # 제곱의 결과를 제곱한다. ((2**2)**2) ...

    return ones

print(get_nth(n)[1][0])