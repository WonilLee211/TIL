# 최대 공약수 구하기 위한 로직

# 유클리드 호제법 재귀함수
def recursive_euclidean(a, b): # a > b 가정
    if a/b == b:
        return b
    
    return recursive_euclidean(b, a % b)

print(recursive_euclidean(15, 9)) # 3

# 일반 코드
def Grtst_common_divisor(a, b): # a > b 가정
    
    while a%b != 0:
        a, b = b, a % b

    return b