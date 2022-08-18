
def extend_paper(width):
    if width == 1:
        return 1
    if width == 2:
        return 3
    return (extend_paper(width -1) + extend_paper(width -2) * 2)

T = int(input())
for tc in range(1, T + 1):
    width = int(input())
    print(f'#{tc} {extend_paper(width)}')

'''
# 메모이제이션 팩토리얼 연습
def facto(n):
    if n >= 2 and len(memo) <= n:
        memo.append(n * facto(n-1))
        return memo[n]
    else:
        return memo[n]


T = int(input())
memo = [1, 1]

for tc in range(1, T + 1):
    n = int(input()) # 10 20 30 40 50 60
    ten = n // 10 # 1 2 3 4 5 6 7
    avle_twnty = ten//2 # 20*20 사각형이 가능한 갯수

    cnt = 0
    # 20*20 종이를 0 ~ avle_twnty개 사용할 때 경우 마다
    for twnty in range(avle_twnty + 1):
        # 20*10의 갯수
        num_ten = ten - twnty * 2
        # 20종이와 10종이 갯수에 따른 조합
        # (총 갯수)!/((20종이갯수)!*(10종이갯수)!)에서 20종이 사용횟수만큼 2의 제곱만큼 증가
        cnt += facto(num_ten + twnty)/(facto(num_ten)*facto(twnty)) * (2**twnty)

    print(f'#{tc} {int(cnt)}')

'''