'''
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
1 ≤ N ≤ 100
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

n = int(input())
star = '*'
blank = ' '

for i in range(n , 0, -1):
    print(star*(n-i) + blank*(2*i-1) + star*(n-i))

print('*' * (2  *n - 1))

for i in range(1, n+1):
<<<<<<< HEAD
    print(star*(n-i) + blank*(2*i-1) + star*(n-i))
=======
    print(star*(n-i) + blank*(2*i-1) + star*(n-i))

>>>>>>> 85ed35442be9133b6947987b18d1660cc286b06d
