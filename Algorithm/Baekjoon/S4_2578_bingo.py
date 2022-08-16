import sys
sys.stdin = open('input.txt')

bingo = [input().split() for i in range(5)]
del_arr = []

for i in range(5):
    del_arr.extend(input().split())
print(bingo)
print(del_arr)

for i in range(15):
    for j in range(5):
        if del_arr[i] in bingo[j]:
            bingo[j].replace(del_arr[i], 0)
            break

print(bingo)