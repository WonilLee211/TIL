# row별 합 중 최대값 반환
def row_sum(li):

    max_sum = 0

    for row in li:
        temp_total = 0
        for num in row:
            temp_total += num
        if temp_total > max_sum:
            max_sum = temp_total

    return max_sum

def max_case(arr):
	# row, column, diagonal 합의 최대값 담을 리스트
    temp_max = [0 for _ in range(4)]

	# zip을 이용하여 매트릭스를 대칭시키고 row_sum함수 재활용
    temp_max[0], temp_max[1] = row_sum(arr), row_sum(list(zip(*arr)))

    # 대각 합 구하기
    for i in range(100):
        temp_max[2] += arr[i][i]
        temp_max[3] += arr[99-i][i]

    # row, column, diagonal 합 중 최대값 인덱스 구하기
    max_sum_idx = 0
    for i in range(1, 4):
        if temp_max[i] > temp_max[max_sum_idx]:
            max_sum_idx = i

    return temp_max[max_sum_idx]

if __name__ == '__main__':

    for _ in range(1, 11):
        test_case = int(input())
        arr = []
        for i in range(100):
            arr.append(list(map(int, input().split())))

        print(f"#{test_case} {max_case(arr)}")