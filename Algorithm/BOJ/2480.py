# 주사위 3개
# 조건 
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
# 입력 주사위 3개 ex 3 3 6
# 출력 : 1300


*_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])
'''
*_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])
구글링해서 알게된 코드
배운점
1. sorted()는 문자열도 정렬한다.
2. sorted()는 리스트로 반환한다.
3. 언패킹 연산자는 앞에 있을 수 있다.
4. 인덱스에서 False는 0, True는 1로 해석된다.
'''
