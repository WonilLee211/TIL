import sys
sys.stdin = open('input.txt')

def postorder(node):
    global stack

    if node and node <= n:
        postorder(c1[node])
        postorder(c2[node])

        if stack:
            if tree[node] in operators and len(stack) > 1:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if tree[node] == '+':
                    result = num1 + num2
                elif tree[node] == '-':
                    result = num1 - num2
                elif tree[node] == '/':
                    result = num1 // num2
                elif tree[node] == '*':
                    result = num1 * num2
                stack.append(result)
            else:
                stack.append(tree[node])
        else:
            stack.append(tree[node])

for tc in range(1, 11):
    n = int(input())

    tree = [''] * (n + 1)
    operators = ['-', '/', '*', '+']

    c1 = [0] * (n + 1)
    c2 = [0] * (n + 1)

    for i in range(1, n + 1):
        li = input().split()
        if li[1] in operators:
            p, op, c1_n, c2_n = int(li[0]), li[1], int(li[2]), int(li[3])
            tree[p] = op
            c1[p] = c1_n
            c2[p] = c2_n
        else:
            p, val = int(li[0]), int(li[1])
            tree[p] = val

    stack = []
    postorder(1)
    print(f'#{tc} {stack[0]}')
