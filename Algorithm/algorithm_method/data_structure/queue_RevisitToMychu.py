'''
queue를 이용한 마이쮸 나눠주기 알고리즘
나눠줄 때마다 나눠주는 마이쮸 개수가 하나씩 증가한다.

'''
from collections import deque
N = 20 # 가지고 있는 마이쮸
m = 0 # 나눠준 마이쮸 수

p = 1 # 처음 줄 설사람 번호
q = deque()
v = 0

while m < N:
    q.append((p, 1, 0)) # 처음 줄 서는 사람, (사람번호, 받아갈 마이쮸 수, m)
    v, c, my = q.popleft()
    print(f'큐에 있는 사람수 {len(q) + 1} 받아갈 사탕 수 {c} 나눠준 사탕 수 {m}')
    m += c
    q.append((v, c + 1, my+c))
    p += 1
print(f'마지막에 받은 사람 : {v}')
