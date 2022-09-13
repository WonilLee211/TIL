import sys
sys.stdin = open('input.txt')

def inorder(n):
    global result

    if n:
        inorder(int(c1[n]))
        result += v[n]
        inorder(int(c2[n]))

for tc in range(1, 11):
    num = int(input())

    c1 = [0] *(num + 1)
    c2 = [0] * (num + 1)
    v = [''] * (num + 1)

    for i in range(1, num +1):
        arr = input().split()
        v[i] = arr[1]
        if len(arr) > 2:
            c1[i] = arr[2]
        if len(arr) > 3:
            c2[i] = arr[3]

    result = ''
    inorder(1)

    print(f'#{tc} {result}')