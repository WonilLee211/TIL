t = 10
for tc in range(1, t + 1):
    dp, mp, m3p, yp = map(int, input().split())
    plan = list(map(int, input().split()))

    min_price = dp * sum(plan)

