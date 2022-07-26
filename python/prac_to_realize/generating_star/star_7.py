'''
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
1 ≤ N ≤ 100
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

'''
n = int(input())
star = '*'
blank = ' '

for i in range(1, n+1):
    print(blank*(n-i) + star*(2*i-1) + blank*(n-i))


for i in range(n - 1, 0, -1):
    print(blank*(n-i) + star*(2*i-1) + blank*(n-i))