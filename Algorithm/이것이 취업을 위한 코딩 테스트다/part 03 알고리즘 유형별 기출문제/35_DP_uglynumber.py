'''

1, 2, 3, 5 만을 소인수로 가지는 수
n번째 소인수를 구하는 프로그램 작성

논리
- 2, 3, 5를 현재 위치에서 곱했을 때 작은 값이 차례대로 들어와야 한다.
- 현재의 값에서 2, 3, 5를 곱해서 비교하게 되면 값 사이에 들어갈 수 있는 다른 못생긴 값이 누락된다.
- 2, 3, 5별로 어떤 위치의 값을 곱했는지 따로 저장한다.
- 각 상황별로 다음에 올 수 있는 숫자들 중 작은 값을 저장한다.
- 선택된 값은 다음에 올 수 있는 값으로 갱신한다.

주의할 점
- next_nums값을 갱신할 때
- [6, 6, 10]과 같이 중복된 값이 있을 수 있다.
- 이를 처리하기 위해서 next_nums와 next_idx를 갱신하는 for-loof 문에서 모든 요소들을 검사해야 한다.
'''

n = int(input())

dp = [0 for i in range(n)]
dp[0] = 1

prime_factors = [2, 3, 5]
next_nums = [2, 3, 5]
next_idx = [0, 0, 0]

for i in range(1, n):
    dp[i] = min(next_nums)              # 다음에 들어갈 값들 중 최소값을 넣기

    for j in range(3):
        if dp[i] == next_nums[j]:       # dp에 저장된 값과 중복된다면 다음 값으로 갱신해주기
            next_idx[j] += 1
            next_nums[j] = dp[next_idx[j]] * prime_factors[j]
            # break                     # 중복된 값이 next_nums에 있을 수 있기 때문에 모든 요소를 비교해서 갱신해야 함

print(dp[-1])
