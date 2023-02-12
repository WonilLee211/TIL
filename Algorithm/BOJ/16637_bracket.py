import sys
sys.stdin = open("input.txt")

n = int(input())
data = list(input())

'''
1. 모든 경우를 탐색한다.
dfs
- 수식 만들기
2. 1 ~ 가장 큰 홀수까지 visited를 찍기 
3. 괄호 내 값을 연산하여 수식 만들기
4. 괄호 케이스 하나당 수식 계산 후 비교
'''


visited = [0] * n
m =  n // 2
max_value = 0
def operate(acc, op, next):
    num = int(next)
    if op == "-":
        acc -= - num
    elif op == "+":
        acc += - num
    else:
        acc *= num
    return acc
def calculate(exp):
    length = len(exp)
    acc = int(exp[0])
    for i in range(1, length, 2):
        acc = operate(acc, exp[i], exp[i + 1])
    return acc

def make_expression(depth, visited, exp):
    global max_value

    if depth == m:
        acc = calculate(exp)
        max_value = max(max_value, acc)

    else:
        for i in range(1, n, 2):
            if (i > 1 and visited[i - 2] == 1) or (i < n - 2 and visited[i + 2] == 1):
                exp.append(data[i])
                exp.append(data[i + 1])
                make_expression(depth + 1, visited, exp)
                continue
            visited[i] = 1
            exp[-1] = operate(exp[-1], data[i], data[i + 1])
            make_expression(depth + 1, visited, exp)
            visited[i] = 0

make_expression(0, visited, data[0])

print(max_value)