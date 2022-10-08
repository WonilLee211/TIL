import sys
sys.stdin = open('input.txt')

def dfs(d, res, a):
    # 깊이가 n이고 모음을 포함하고, 모음을 제외한 길이가 2이상일 때 출력
    if d == n and set(res) & vowel and len(res) - len(set(res).intersection(vowel)) > 1:
        print(res)
        return
    else:
        for i, s in enumerate(a):
            dfs(d + 1, res + s, a[i+1:])

n, m = map(int, input().split())
vowel = set('aeiou')
a = input().split()
a.sort()
dfs(0, '', a)
