# 20개의 비트가 모두 켜진 수
pizza = (1<<20) - 1 # 1048575

#비트 추가
# p번 비트는 반드시 켜기
pizza = (1<<5) # 100000
p = 3
pizza |= 1 << p # or 연산자
print(True) if pizza&(1<<p) else print(False)

# 비트 삭제
# 첫번째 방법 : 1을 포함할 때만
pizza -= (1<<p)

# 두번째 방법
pizza |= (1 << p) # or 연산자
pizza &= ~(1 << p)
# ~(1<<3) : 1000 비트의 전체비트 전환하고 & 연산
# p번 비트를 제외하고 모두 유지되고 p번 비트는 0
print(True) if pizza&(1<<p) else print(False)

# 세번째 방법 :XOR : 켜져있으면 끄고 꺼져있으면 켜기
pizza |= (1 << p) # or 연산자
pizza ^= (1 << p)

# 집합 현산
a = 1 << 5 - 1
b = 60
added = a | b # 교집합
intersection = a & b # 합집합
removed = a & ~b # a에서 b를 뺀 집합
toggled = a ^ b # 합집합에서 교집합을 뺀 집합

# 집합 크기 구하기
def bitcount(x):
    if not x: return 0
    return x%2 + bitcount(x//2)

print(bitcount((1<<4) -1))
