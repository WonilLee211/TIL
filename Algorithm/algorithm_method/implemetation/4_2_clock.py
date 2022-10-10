# 0시 0분 0초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
# 논리
# 모든 경우의 수는 24 * 60 * 60 = 86400가지로 2초(200000) 안에 해결 가능

n = int(input())

cnt = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)