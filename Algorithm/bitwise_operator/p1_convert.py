import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    data = input()
    n = len(data)

    i = 0
    dec = 0
    ans = []
    while i < n:
        if data[i] == '1':
            dec += 2**(6-i%7)
        
        i += 1

        if i%7==0:
            ans.append(dec)
            dec = 0
            
    print(*ans)


        
    
