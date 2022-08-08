# 검사할 세대에  (-2 ~ 2) 범위 사이에서 가장 높은 건물 찾기
def max_height(i, arr):
    max_h = 0
    for j in [1, 2, -1, -2]:
        # i+1, i+2, i-1, i-2
        if arr[i + j] > max_h:
            max_h = arr[i + j]
    return max_h

def view(N, arr):
    cnt = 0
		# 0 , n-2, n-1 인덱스의 배열 값은 0이므로 검사할 필요가 없음
    for i in range(2, N-2):
        max_h = max_height(i, arr)
				#범위내에 건물줄 제일 높은 곳보다 높다면 조망권 확보
        if arr[i] > max_h:
            cnt += arr[i] - max_h
    return cnt

if __name__ == '__main__':
    T = 10
    for test_case in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        print(f'#{test_case} {view(N, arr)}')
