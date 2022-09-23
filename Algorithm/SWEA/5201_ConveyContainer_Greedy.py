import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())        # 컨테이너 수, 트럭 수
    w = list(map(int, input().split()))     # 컨테이너별 무게
    t = list(map(int, input().split()))     # 트럭별 적재 용량
    w.sort(reverse=True)
    t.sort(reverse=True)

    total = 0
    for i in range(len(w)):
        j = 0
        while j < m:

            if w[i] <= t[j]:
                total += w[i]
                t[j] = 0
                break

            j += 1

    print(f'#{tc} {total}')