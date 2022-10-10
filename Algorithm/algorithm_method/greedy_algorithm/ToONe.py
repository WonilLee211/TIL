#이것이 취업을 위한 코딩테스트다_그리디
# 일이 될 때까지

# n이 1이 될 때까지 아래 연산
# n이 k로 나눠떨어지는 수라면 나누기
# 아니라면 -1

n, k = 25, 3

cnt = 0
while True:
    t, v = divmod(n, k)

    if t == 0:
        if v > 1:
            cnt += v - 1
        break

    cnt += v + 1
    n = t

print(cnt)
