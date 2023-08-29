'''
와일드카드 문자열과 함께 파일명의 집합이 주어질 때,
 그 중 매치되는 파일명들을 찾아내는 프로그램을 작성

와일드 카드 he?p 는 파일명 help 에도, heap 에도 매치되지만, helpp 에는 매치되지 않는다.
 와일드 카드 *p* 는 파일명 help 에도, papa 에도 매치되지만, hello 에는 매치되지 않는다.
'''

'''
*에 몇 개의 글자가 대응되어야 하는지 미리 알 수 없다.
가장 쉬운 방법 : 완전 탐색
패턴 내에 *가 나올 때마다 서브패턴이 문자열에 포함되는지 확인
'''
import sys
sys.stdin = open('input.txt')

def match_memo(w, s):
    return

    w = input()


for tc in range(1, int(input()) + 1):

    n = int(input())
    for i in range(n):
        s = input()
        if match(w, s):
            print(s)

'''
def match(w, s): # 와일드카드 패턴 w가 문자열 s에 대응하는지 여부 반환
    pos = 0
    # w[pos]와 s[pos] 매칭해나가기
    while pos < len(s) and pos < len(w) and (w[pos] =='?' or w[pos] == s[pos]):
        pos += 1
    # 매칭이 끝난 이유에 따라 처리
    # 2. 패턴 끝에 도달해서 끝난 경우 남은 문자열 길이와도 일치해야 매칭됐을 것!
    if pos == len(w):
        return pos == len(s)
    # 4. *를 만나서 끝난 경우 *에 몇글자를 대응할지 완전 탐색
    if w[pos] == '*':
        skip = 0
        while pos + skip <= len(s):
            if match(w[pos + 1:], s[pos + skip:]):
                return True
            skip += 1
    # 이 외의 경우에 대해서는 실패
    return False

for tc in range(1, int(input()) + 1):
    w = input()

    n = int(input())
    for i in range(n):
        s = input()
        if match(w, s):
            print(s)
'''