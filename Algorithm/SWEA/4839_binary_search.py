'''
책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 
이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력. 
비긴 경우는 0을 출력
'''

# 타겟을 찾는데 걸린 탐색 횟수 구하는 함수
def searching(target, L, R):
    cnt = 0
    # 이진탐색알고리즘
    while True:
        mid_p = (L + R) // 2
        if target > mid_p:
            L = mid_p
            cnt += 1
        elif target < mid_p:
            R = mid_p
            cnt += 1
        else:
            return cnt

def page_search(pages, a ,b):
    L, R, cnt_a, cnt_b = 1, pages, 0, 0

    # a와 b의 탐색 횟수
    cnt_a = searching(a, L, R)
    cnt_b = searching(b, L, R)

    # 승자 판단
    if cnt_a > cnt_b:
        return "B"
    elif cnt_a < cnt_b:
        return "A"
    else:
        return 0

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        P, A, B = map(int, input().split())
        print(f"#{test_case} {page_search(P, A ,B)}")