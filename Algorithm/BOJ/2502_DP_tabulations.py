import sys
sys.stdin = open('input.txt')

# tabulations을 이용한 피보나치 수열
def tabulations(table, fst, scnt):

    table[0], table[1] = fst, scnt
    for i in range(2, d):
        table[i] = table[i-1] + table[i-2]

    return table[-1]

d, k = map(int, input().split())

tabul = [0] * d

# 검사 초기값
fst = scnt = 1

while True:
    result = tabulations(tabul, fst, scnt)

    if result > k:          # 결과 값이 찾는 값보다 클 때
        fst += 1            # 첫 날 떡 수 증가
        scnt = fst          # 둘째 날 떡 수도 첫날과 동일하게 맞추기
        continue
    elif result == k:       # 예상이 맞을 경우
        break

    scnt += 1               # 결과 값이 찾는 값보다 작을 땐 둘째 날 떡 수만 증가시키기

print(fst)
print(scnt)
