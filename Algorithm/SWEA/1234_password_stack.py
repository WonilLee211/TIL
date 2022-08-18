
def del_repeated_num(string, n):
    string = string
    stack = [' ']
    for i in range(n):
        if stack[-1] == string[i]:
            stack.pop()
        else:
            stack.append(string[i])

    return stack

if __name__ == '__main__':
    for tc in range(1, 11):
        n, string = input().split()
        result = ''.join(del_repeated_num(string, int(n))[1:])
        print(f'#{tc} {result}')
