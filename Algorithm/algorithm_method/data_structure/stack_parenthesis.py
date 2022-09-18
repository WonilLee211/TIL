# ()()((()))

def test_parenthesis(paren):
    stacksize = len(paren)
    stack = [''] * stacksize
    top = -1
    for i in range(len(paren)):
        if paren[i] == '(':
            top += 1
            stack[top] = '('
        else:
            if stack[top] == '(':
                top -= 1
            else:
                return -1 #'underflow' 열리는 괄호가 없는 경우

    if top != -1:
        return -1 # 'overflow' 닫히는 괄호가 없는 경우

    return 1

T = int(input())
for tc in range(T):
    paren = input()
    print(test_parenthesis(paren))