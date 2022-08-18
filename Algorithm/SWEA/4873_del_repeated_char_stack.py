def del_repeat_char(string):
    top = 1
    stack = ' ' + string[0]

    i = 1
    while i < len(string):

        if string[i] != stack[top]:
            top += 1
            stack += string[i]
        else:
            stack = stack[:top]
            top -= 1

        i += 1

    return len(stack[1:])


if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):
        string = input()
        print(f'#{tc} {del_repeat_char(string)}')