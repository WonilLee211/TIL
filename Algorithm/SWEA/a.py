
def f1(i, k, t): # 재귀횟수, 목표횟수, 목표 합
    global cnt
    if i == k:
        s = 0
        for j in range(10):
            if bit[j]:
                s += arr[j]
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(arr[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i + 1, k, t)
        bit[i] = 1
        f1(i + 1, k, t)

def f2(i, k, t, s, rs): # 재귀횟수, 목표횟수, 목표 합, 지금까지의 합
    global cnt
    cnt += 1

    if s > t:
        return
    if t > s + rs:
        return

    if i == k:
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(arr[j], end = ' ')
            print()
    else:
        bit[i] = 0
        f2(i + 1, k, t, s, rs - arr[i])
        bit[i] = 1
        f2(i + 1, k, t, s + arr[i], rs - arr[i])


arr = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
# f1(0, 10, 10)
f2(0, 10, 10, 0, sum(arr))
print(cnt)