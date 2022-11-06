
import sys
sys.stdin = open('input.txt')

s = input()

length = len(s)
unit_range = length // 2

answer = length

for i in range(1, unit_range + 1):
    cnt = 1
    compressed = ''

    fr, to = 0, i
    pattern = s[fr:to]

    while to + i < length:

        if pattern == s[to: to + i]:
            cnt += 1
        else:
            if cnt == 1:
                compressed += pattern
            else:
                compressed += str(cnt) + pattern
            cnt = 1
            pattern = s[to:to + i]

        fr, to = to, to + i

    if cnt != 1:
        compressed += str(cnt) + pattern

    answer = min(answer, len(compressed))


print(answer)