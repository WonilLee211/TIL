'''
첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
별은 가운데를 기준으로 대칭이어야 한다..
1 ≤ N ≤ 100
첫째 줄부터 N번째 줄까지 차례대로 별을 출력.
'''

n = int(input())
star = '*'
blank = ' '

for i in range(n, 0, -1):
    print(blank*(n-i) + star*i + blank*(n-i))
    
