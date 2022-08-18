
T = int(input())
for tc in range(1, T+1):
    line = input()
    stack = []

    for elem in line:
        if elem == '(' or elem == '{':
            stack.append(elem)
        elif elem == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(elem)
                break
        elif elem == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(elem)
                break

    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

'''
# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램

def is_parenthesis(string):
    stack = []

    open_paren = ['{', '(', '[']
    close_paren = ['}', ')', ']']

    i = 0
    while i < len(string):
        # i번째 문자가 괄호인 경우에만 고려
        if string[i] in open_paren or string[i] in close_paren:
            # 여는 괄호 없이 닫힌 괄호가 입력됐을 때 미스매칭
            if len(stack) == 0 and string[i] in close_paren:
                return 0
            # 여는 괄호 일 때 스택에 저장
            if string[i] in open_paren:
                stack.append(string[i])

            # 닫히는 괄호 일 때
            elif string[i] in close_paren:

                # 유니코드 수 사용
                # print(ord('('), ord(')')) # 40 41
                # print(ord('{'), ord('}')) # 123 125
                if (ord(string[i]) - 1) == ord(stack[-1]) or (ord(string[i]) - 2) == ord(stack[-1]):
                    if len(stack) != 0: # 스택에 여는 괄호가 있으면 팝
                        stack.pop()
                    else: # 없으면 미스매칭
                        return 0
                else: # 괄호가 유니코드 수의 차이로 일치하지 않으면 미스매칭
                    return 0
        i += 1

    if len(stack) == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):
        string = input()
        print(f'#{tc} {is_parenthesis(string)}')
'''