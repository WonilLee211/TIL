import sys, pprint
sys.stdin =open('input.txt')


import copy

n = int(input())

dice = [0] * n

for i in range(n):
    dice[i] = [0] + list(map(int, input().split()))

link = {1:6, 2:4, 3:5, 4:2, 5:3, 6:1} # 연결된 인덱스...
cnt_max = [0] * 6

for i in range(1, 7): # 일층 주사위 윗면 숫자의 인덱스 결정
    temp = copy.deepcopy(dice)

    dice_bt = temp[0][i]
    dice_top = temp[0][link[i]]

    j = 0
    while True:
        temp[j].remove(dice_top)
        temp[j].remove(dice_bt)

        cnt_max[i - 1] += max(temp[j])

        if j + 1 == n:
            break
        else:
            j += 1
            dice_bt = temp[j][temp[j].index(dice_top)]
            dice_top = temp[j][link[temp[j].index(dice_bt)]]

print(max(cnt_max))

