import sys
sys.stdin = open('input.txt')

n = int(input())
# 인덱스 번호와 카드 번호 맞추기
card_prices = [0] + list(map(int, input().split()))

ppc = [0] + [card_prices[i]/i for i in range(1,n+1)]
print(ppc)