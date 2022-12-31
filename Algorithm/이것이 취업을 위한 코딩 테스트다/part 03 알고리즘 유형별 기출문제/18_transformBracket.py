import sys
sys.stdin = open('input.txt')

'''
소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램

'(' 와 ')' 로만 이루어진 문자열이 있을 경우, 
- 균형잡힌 괄호 문자열 : '(' 의 개수와 ')' 의 개수가 같을 경우 
- 올바른 괄호 문자열 : '('와 ')'의 괄호의 짝도 모두 맞을 경우

균형잡힌 괄호 문자열을 올바른 괄호 문자열로 변환하기
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

입력 : "균형잡힌 괄호 문자열" p가 매개변수로 주어짐, 2 <= len(p) <= 1000 짝수

출력 : "올바른 괄호 문자열"로 변환한 결과
이미 "올바른 괄호 문자열"이라면 그대로 return 하면 됩니다.

p : result
"(()())()" :	"(()())()"
")(" :	"()"
"()))((()" :	"()(())()"


논리
1. 입력된 문자열이 올바른 문자열인지 판단하는 함수 만들기
2. 올바른 문자열이 아닌 경우
    1. 균형 문자열 u, v로 나누기
    
2. 균형 문자는 u에 저장
3. 불균형 문자는 

'''

p = "()))((()"

ans = ""

def is_right(balance_str): # 균형잡힌 문자열 : 열고 닫는 괄호 개수가 일치함

    cnt_open_racket = 0

    for sub in balance_str:
        if sub == "(":
            cnt_open_racket += 1
        else:
            if cnt_open_racket == 0: # 닫는 괄호인데 매칭되는 여는 괄호가 없다면 옳지않은 문자열
                return False
            else:
                cnt_open_racket -= 1

    return True # 모두 통과한다면 올바른 괄호 문자열

def make_balanced_string(wrong_str):

    u, v = "", ""
    size = len(wrong_str)
    is_balance = 0

    for idx, sub in enumerate(wrong_str):
        u += sub

        is_balance += 1 if sub == "(" else -1

        if is_balance == 0 and size - 1 != idx:
            v = wrong_str[idx + 1:]
            break

    return u, v

def reverse_bracket(bracket):
    acc = ""
    for sub in bracket[1:-1]:
        acc += ")" if sub == "(" else "("

    return acc


def make_right_string(wrong_str):

    if wrong_str == "":
        return ""

    u, v = make_balanced_string(wrong_str)

    if is_right(u):
        return u + make_right_string(v)
    else:
        return "(" + make_right_string(v) + ")" + reverse_bracket(u)

ans = make_right_string(p)






