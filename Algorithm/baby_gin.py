# baby-gin game
'''
- 0~9 사이 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라 한다.
- 그리고 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
- 6개의 숫자를 입력받아 baby-gin 여부를 판단하는 프로그램 작성

내가 생각한 방법
1. 카운팅 알고리즘을 사용
2. cnt_arr에서 3이 있다면 triplet
3. cnt_arr에서 요소들이 연속되어 있다면 run
4. 둘다 해당하거나  둘의 요소가 2개씩 있거나 하면 baby-gin
'''


def baby_gin(num):
    # 뒤에 비교 과정에서 인덱스 에러 방지를 위해 12자리 공간 만들기
    cnt_arr = [0 for _ in range(12)]
    # num의 각 자리 수를 인덱스로 사용하여 cnt_arr에 갯수 세기
    for i in range(6):
        cnt_arr[num % 10] += 1
        num //= 10

    triplet = run = 0
    i = 0
    # 2개의 조건을 한번에 적용하기 위해 while 문 사용
    while i < 10:
        # triplet 조건
        if cnt_arr[i] >= 3:
            cnt_arr[i] -= 3
            triplet += 1
            continue

        # run 조건
        if cnt_arr[i] >= 1 and cnt_arr[i + 1] >= 1 and cnt_arr[i + 2] >= 1:
            cnt_arr[i] -= 1
            cnt_arr[i + 1] -= 1
            cnt_arr[i + 2] -= 1
            run += 1
            continue  # 값을 뺀 다음 같은 인덱스 위치에서 다른 조건에서 만족하는지 보기 위해 continue
        i += 1

    return 1 if (triplet and run) or triplet == 2 or run == 2 else 0