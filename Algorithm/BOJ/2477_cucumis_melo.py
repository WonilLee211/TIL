import sys
sys.stdin = open('input.txt')

unit = int(input())

arr = []
for _ in range(6):
    arr.append(list(map(int, input().split())))

for i in range(6):
    if arr[i%6][0] == 4 and arr[(i+1)%6][0] != 2:
        small1, small2 = arr[i%6][1], arr[(i+1)%6][1]
        direc1, direc2 = 3, 2
        break
    elif arr[i%6][0] == 2 and arr[(i+1)%6][0] != 3:
        small1, small2 = arr[i%6][1], arr[(i+1)%6][1]
        direc1, direc2 = 1, 3
        break
    elif arr[i%6][0] == 3 and arr[(i+1)%6][0] != 1:
        small1, small2 = arr[i%6][1], arr[(i+1)%6][1]
        direc1, direc2 = 4, 1
        break
    elif arr[i%6][0] == 1 and arr[(i+1)%6][0] != 4:
        small1, small2 = arr[i%6][1], arr[(i+1)%6][1]
        direc1, direc2 = 2, 4
        break


big1 = big2 = 0
for dir, value in arr:
    if dir == direc1:
        big1 = value
    if dir == direc2:
        big2 = value

total_arr = (big1*big2 - small1*small2 ) * unit

print(total_arr)