'''
다단계 칫솔 판매 수익 계산

논리
- 자식에서 부모로 수익을 거슬러 올라가 넘겨줘야하기 때문에
- 자식 to 부모를 찾을 수 있는 연결 리스트를 만들어야 함
- 루트까지 도달할 때까지 수익 계산

주의점
- profit이 0이 될 때 break함으로써 시간을 줄임

'''

def solution(enroll, referral, seller, amount):

    n = len(enroll)
    answer = [0 for _ in range(n)]

    # child to parent 연결리스트 만들기
    childToParent = ['' for _ in range(n)]

    nums = {}
    for i in range(n):
        nums[enroll[i]] = i

    for i in range(n):
        if referral[i] != '-':
            childToParent[i] = nums[referral[i]]

    m = len(seller)

    for i in range(m):
        amount[i] *= 100

    for i in range(m):
        salesman, profit = nums[seller[i]], amount[i]
        answer[salesman] += (profit - profit // 10)
        profit = profit // 10

        while childToParent[salesman] != '':
            answer[childToParent[salesman]] += (profit - profit // 10)
            salesman, profit = childToParent[salesman], profit // 10
            if profit == 0:
                break
    return answer