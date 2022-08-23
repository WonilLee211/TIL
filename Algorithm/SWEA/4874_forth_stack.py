T = int(input())
for tc in range(1, T+1):
    operators = ['+', '-', '/', '*', '(']
    temp = []
    postfix_arr = input().split()[:-1]
    result = None
    # 후위 표기법의 수식을 스택을 이용하여 계산하기

    i = 0
    while i < len(postfix_arr):
        x = postfix_arr[i]
        if x not in operators: # 숫자
            temp.append(x)
            i += 1
        else: # 연산자 및 괄호
            if len(temp) > 1 and temp[-1] not in operators and temp[-2] not in operators:
                B = int(temp.pop())
                A = int(temp.pop())

                if x == '-':
                    temp.append(A - B)
                elif x == '+':
                    temp.append(A + B)
                elif x == '/':
                    temp.append(A // B)
                elif x == '*':
                    temp.append(A * B)
                i += 1

            else:
                result = 'error'
                break

    if len(temp) != 1:
        result = 'error'

    if result != 'error':
        result = temp.pop()
    print(f'#{tc} {result}')