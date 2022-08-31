T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    stop = [0] * 1001

    for _ in range(n):
        bus, a, b = map(int, input().split())
        stop[a] += 1
        stop[b] += 1
        if bus == 1:
            for i in range(a + 1, b):
                stop[i] += 1

        elif bus == 2:
            if a % 2 == 0:
                for i in range(a + 1, b):
                    if i % 2 == 0:
                        stop[i] += 1
            else:
                for i in range(a + 1, b):
                    if i % 2 == 1:
                        stop[i] += 1
        elif bus == 3:
            if a % 2 == 0:
                for i in range(a+1, b):
                    if i % 4 == 0:
                        stop[i] += 1
            else:
                for i in range(a + 1, b):
                    if i % 3 == 0 and i % 10 != 0:
                        stop[i] += 1

    print(f'#{tc} {max(stop)}')