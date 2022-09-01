import sys
sys.stdin =open('input.txt')

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))

for i in range(1<<9):
    combination = []
    cnt = 0
    for j in range(9):
        if i & (1<<j):
            combination.append(dwarf[j])
            cnt += dwarf[j]
    if cnt == 100 and len(combination) == 7:
        break
#
# for i in range(6):
#     min_idx = i
#     for j in range(i+1, 7):
#         if combination[j] < combination[min_idx]:
#             min_idx = j
#     combination[i], combination[min_idx] = combination[min_idx], combination[i]

print(*combination, sep='\n')