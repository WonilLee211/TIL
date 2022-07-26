n = int(input())
star = '*'
blank = ' '

for i in range(1, n+1):
    print(blank*(n-i) + star*(2*i-1) + blank*(n-i))


for i in range(n - 1, 0, -1):
    print(blank*(n-i) + star*(2*i-1) + blank*(n-i))