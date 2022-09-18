# 입력받은 10진수를 2진수로 바꾸기

def dec_to_bin(n):
    if n < 2:
        return str(n)
    
    # 몫과 나머지
    t, v = divmod(n, 2)
    return dec_to_bin(t) + dec_to_bin(v)

if __name__ == '__main__':
    N = int(input())
    print(dec_to_bin(N))
