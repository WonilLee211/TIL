import sys
sys.stdin = open('input.txt')

from collections import deque

# k진수 변환 함수
def dectobin(n, k):
    if n < k:
        return str(n)
    else:
        return dectobin(n // k, k) + dectobin(n % k, k)

def solution(n, k):
    bin = dectobin(n, k)
    q = deque(bin)
    q.append('0')

    stack = ''
    cnt = 0

    while q:
        n = q.popleft()
        if int(n):
            stack += n

        elif stack and n == '0': # 예외처리 stack이 채워져있고, n == 0이고
            if stack != '1': # stack이 '1'이 아닐 때
                p = int(stack)
                flag = True
                # 나눠지는 값이 있으면 cnt 안함
                for s in range(2, int(p ** 0.5) + 1):
                    if not (p % s):
                        flag = False
                        break
                if flag:
                    cnt += 1

            stack = ''

    return cnt
