import sys
sys.stdin = open('input.txt')

n = int(input())
# 인덱스 번호와 카드 번호 맞추기
card_prices = [0] + list(map(int, input().split()))

ppc = [0] *(n + 1)
res = n
total = 0

for i in range(1, n + 1):
    ppc[i] = card_prices[i]/i 

while res > 0:
    max_i = res
    max_p = ppc[max_i]

    for i in range(1, res):
        if ppc[i] > max_p:
            max_p = ppc[i]
            max_i = i

    total += card_prices[max_i]*(res//max_i)
    res %= max_i

print(int(total))