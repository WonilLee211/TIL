'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
'''


def card(number, N):
    cnt_list = [0 for _ in range(10)]
    t = number

    for _ in range(N):
        cnt_list[t % 10] += 1 # 나머지 값을 인덱스로서 위치에 카운팅
        t //= 10 # 몫 최신화

    max_idx = 9
    for i in range(8, -1, -1): # 뒤에서부터 접근하여 같은 횟수의 숫자 중 큰 값이 출력되도록 
        if cnt_list[i] > cnt_list[max_idx]:
            max_idx = i

    return max_idx, cnt_list[max_idx]

if __name__=="__main__":

    T = int(input())
    for test_case in range(1, T +1):
        N = int(input())
        number = int(input())
        res = card(number, N)
        print(f'#{test_case} {res[0]} {res[1]}')