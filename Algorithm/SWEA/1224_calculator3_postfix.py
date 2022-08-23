
for tc in range(1, 11):
    # 1. 후위 표기법 만들기
    n = int(input())
    state = input()

    # 토큰:[isp, icp]
    priority = {'+': [1, 1], '-': [1, 1], '/': [2, 2], '*': [2, 2], '(': [0, 3]}
    operators = ['+', '-', '/', '*', '(']
    stack = []
    postfix_arr = []

    for x in state:
        # 1.1 ')'일 때
        if x == ')':
            while len(stack) > 0 and stack[-1] != '(':
                postfix_arr.append(stack.pop())
            stack.pop() # '(' 빼내기

        #  1.2 ')'를 제외한 연산자 만난 경우
        elif x in operators:
            while len(stack) > 0 and priority[stack[-1]][0] >= priority[x][1]:
                top = stack.pop()
                if top != '(':
                    postfix_arr.append(top)
            stack.append(x)  # 우선순위에 따라 stack에 pop 시킨 후 stack에 연산자 넣기

        # 1.3 숫자일 때 바로 배열에 저장
        else:
            postfix_arr.append(x)

    while stack:  # 스택에 남아있는 연산자 ( 빼고 배열에 저장
        top = stack.pop()
        if x != '(':
            postfix_arr.append(top)

    # 2. 후위 표기법의 수식을 스택을 이용하여 계산하기
    temp = []
    i = 0
    while i < len(postfix_arr):
        x = postfix_arr[i]
        if x not in operators:
            temp.append(x)
            i += 1
        else:
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

    result = temp.pop()
    print(f'#{tc} {result}')