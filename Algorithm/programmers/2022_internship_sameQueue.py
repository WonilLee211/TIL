
'''
1 <= len(q) <= 300,000
1 <= q[x] <= 10**9

논리
- 두 값의 총합의 절반이 되어야 한다.
- 그룹을 한 개 부터 n-1개까지
- 각 그룹별로 초기에 합을 구하고
- 순환하면서 다음값 더하고 마지막값 빼고 결과가 절반이 맞는지 확인
- 끝까지 돌았는데 답이 안나오면 Return -1

'''

from collections import deque

def solution(queue1, queue2):

    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    iteration = len(queue1) * 4
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    sum_q = sum_q1 + sum_q2

    if sum_q % 2 != 0:
        return -1

    while True:
        if sum_q1 > sum_q2:
            pop_value = queue1.popleft()
            queue2.append(pop_value)
            sum_q1 -= pop_value
            sum_q2 += pop_value

        elif sum_q1 < sum_q2:
            pop_value = queue2.popleft()
            queue1.append(pop_value)
            sum_q2 -= pop_value
            sum_q1 += pop_value

        else:
            return answer

        answer += 1

        if answer == iteration:
            return -1
