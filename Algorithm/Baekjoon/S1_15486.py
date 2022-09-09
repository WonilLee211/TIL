import sys
sys.stdin = open('input.txt')

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
