
'''
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''
def unusual_sort(arr, N):

    unusual_arr = []

    # 최대값 최소값 저장을 5번 반복
    for _ in range(5):
        max_idx = 0
        # 선택정렬 알고리즘을 이용한 맥스인덱스 구하기
        for j in range(1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        # 원본에서 최대값을 빼내서 unusaul_arr에 저장하기
        unusual_arr.append(arr.pop(max_idx))

        # 상동
        min_idx = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        unusual_arr.append(arr.pop(min_idx))

    return unusual_arr

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))

        res = unusual_sort(arr, N)
        result = ''
        for x in res:
            result += str(x) + " "

        print(f"#{test_case} {result[:-1]}")
