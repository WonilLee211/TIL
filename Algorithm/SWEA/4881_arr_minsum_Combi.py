# p[] : 데이터가 저장된 배열
# k : 원소의 개수, i : 선택된 원소의 인덱스
def perm(i, k):
    global minV
    if i == k:      # 인덱스 i == 원소의 개수
        s = 0       # 모든 l행에서 p[l]열을 골랐을 때의 합
        for l in range(k):
            s += arr[l][p[l]]
        if minV > s:
            minV = s
        elif s >= minV:     # 백트래킹
            return
        else:
            for j in range(i, k):
                p[j], p[i] = p[i], p[j]
                perm(i + 1, k)
                p[j], p[i] = p[i], p[j]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n) ]
    p = [i for i in range(n)]         # p[i] i행에서 선택한 열 번호
    minV = n * 10

    perm(0, n)
    print(f'#{tc} {minV}')