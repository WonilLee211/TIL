
t = int(input())

for tc in range(1, t+1):
    n = int(input())

    prices = list(map(int,input().split()))

    max_price = prices[-1]
    buy_list = buy_cnt = 0
    earning = 0

    # 뒤에서부터 가격 확인
    for i in range(n-2, -1, -1):
        # 현재 가격보다 싸다면 구매 시점
        if prices[i] <= max_price:
            buy_list += prices[i]
            buy_cnt +=1

        else: # 현재 가격보다 비싸다면 판매시점
            earning += max_price * buy_cnt - buy_list
            buy_list = buy_cnt = 0
            max_price = prices[i]

        if not i: # i = 0일 때 판매를 통해 정산
            earning += max_price * buy_cnt - buy_list
            break

    print(f"#{tc} {earning}")