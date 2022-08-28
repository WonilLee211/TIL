import sys
sys.stdin = open('input.txt')


'''
시간초과
def combination(arr, n, r):
    result = []

    if r > n:
        return result

    if r == 1:
        for i in arr:
            result.append([i])

    elif r > 1:
        for i in range(n - r + 1):
            for j in combination(arr[i+1:], n-1, r-1):
                result.append([arr[i]] + j)
    return result
'''

import itertools

n = int(input())

arr = list(range(1, n + 1))

synergy = [[0] * (n+1)] + list([0]+list(map(int, input().split())) for i in range(n))
team_case = []

for i in itertools.combinations(range(1, n + 1), n//2):
    team_case.append(list(i))


min_diff = 0
for row in synergy:
    min_diff += sum(row)

for team1 in team_case:
    team2 = list(set(arr) - set(team1))

    total1 = total2 = 0
    for i in range(len(team1)-1):
        for j in range(i + 1, len(team1)):
            total1 += synergy[team1[i]][team1[j]] + synergy[team1[j]][team1[i]]
            total2 += synergy[team2[i]][team2[j]] + synergy[team2[j]][team2[i]]

    if abs(total1 - total2) < min_diff:
        min_diff = abs(total1 - total2)

print(min_diff)