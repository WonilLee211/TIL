import sys
sys.stdin = open('input.txt')

n = int(input())
ldtms = [0] * n
p = [0] * n

for i in range(n):
    ldtms[i], p[i] = map(int, sys.stdin.readline().split())

dplist = [0] * (n + 1)
# dplist[i + ldtms[i]]
# = 오늘부터 ldtms[i]일동안 일하지 않았을 때와 일할 때
#   (i + ldtm[i])날 가질 돈 중 큰 값
# dplist[i + ldtms[i]] = max(dplist[i] + p[i], dplist[i+ ldtms[i]])
# earn
# = 현재까지 벌 수 있는 수입의 경우 중 최대 값
# earn = max(dplit[i], earn)
earn = 0
for i in range(n):
    earn = max(dplist[i], earn)

    if ldtms[i] + i <= n:
        dplist[i + ldtms[i]] = max(earn + p[i], dplist[i + ldtms[i]])

print(max(dplist))

'''시간초과
def dfs(day, total):
    global max_total

    total += prices[day]
    
    if max_total > total + sum(prices[day+1:]):
        return

    if day + leadtimes[day] < n:
        dfs(day + leadtimes[day], total)
        dfs(day + 1, total - prices[day])
    else:
        if total > max_total:
            max_total = total
            return
        return

n = int(input())
leadtimes = [0] * n
prices = [0] * n

for i in range(n):
    day, price = map(int, input().split())
    
    if i + day > n:
        price = 0
    leadtimes[i], prices[i] = day, price

max_total = 0
dfs(0, 0)
print(max_total)
'''