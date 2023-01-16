'''
1. 1번부터 먹기 시작. 번호가 증가하느 순서대로 배열됨
2. 마지막 번호의 음식을 섭취한 뒤 회전판에 의해 다시 1번 음식이 무지 앞으로 옮
3. 1초동안 음식을 섭취한 뒤 다시 다음 음식 섭취
4. k 초 후에 중단
5. 다음 음식을 뭘 먹어야 하는지?

k초보다 음식의 시간의 최소값이 작다면

k초가
'''
import heapq

food_times = [3, 1, 2]
k = 5
n = len(food_times)
if k >= sum(food_times):
    print(-1)

q = []
for i in range(n):
    heapq.heappush(q, (food_times[i], i + 1))

acc_time = 0
previous = 0

while acc_time + (q[0][0] - previous) * n <= k:
    t, idx = heapq.heappop(q)
    acc_time += (t - previous) * n
    n -= 1
    previous = t

result = sorted(q, key=lambda x: x[1])
print(result[(k - acc_time) % n][1])