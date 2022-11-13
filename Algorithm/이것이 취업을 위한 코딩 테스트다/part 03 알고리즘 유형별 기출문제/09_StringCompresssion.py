
import sys
sys.stdin = open('input.txt')

s = input()
'''
논리
- 일단 문자열 길이의 절반 초과의 길이는 압축 단위가 되지 못한다.
- 압축 단위 1 ~ length // 2
- 압축 단위별로 
    - 현재 패턴과 앞 문자가 같을 때
        - 카운트
    - 다를 때
        - comp에 cnt + pattern (cnt == 1, + pattern)
        -  cnt 초기화pattern 변경
    - 인덱스 변경
- 끝값 처리
    - 마지막에 패턴와 남은 문자열 길이가 딱맞게 안떨어지는 경우 처리
    
'''

length = len(s)
unit_range = length // 2

answer = length

for i in range(1, unit_range + 1):
    cnt = 1
    compressed = ''

    fr, to = 0, i
    pattern = s[fr:to]

    while to < length:

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
    # 마지막에 패턴의 길이가 딱맞게 안떨어지는 경우
    if to + i >= length:
        if cnt != 1:
            compressed += str(cnt) + pattern
        else:
            compressed += pattern + s[to:]

    answer = min(answer, len(compressed))


print(answer)