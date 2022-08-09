'''
최고점 블럭을 최저점으로 옮겨 평탄화하는 프로그램
[제약 사항]
가로 길이는 항상 100
모든 위치에서 상자의 높이 : 1이상 100
덤프 횟수 : 1이상 1000

주어진 덤프 횟수만큼만 평탄화
그 때의 최고점과 최저점의 높이 차를 반환

[입력]
총 10개의 테스트 케이스
각 테스트 케이스의 첫 번째 줄 : 덤프 횟수
다음 줄에 각 상자의 높이값

[출력]
#테스트 케이스의 번호 (테스트 케이스의 최고점과 최저점의 높이 차)
'''

# 배열에서 값이 가장 큰 값의 인덱스와 가장 작은 값의 인덱스 반환하는 함수
def min_max(numbers):

    min_idx = 99
    max_idx = 0
    i = 0

    while i < 100:
        if numbers[i] > numbers[max_idx]:
            max_idx = i

        if numbers[i] < numbers[min_idx]:
            min_idx = i

        i += 1 # 0 ~ N-1까지 반복
    return max_idx, min_idx

def flatten(numbers, N):

    for _ in range(N): # 덤핑 반복 횟수
        max_idx, min_idx = min_max(numbers)
        # 최대 최소 인덱스에 대해서 배열의 값 증감 시키기
        numbers[max_idx], numbers[min_idx] = numbers[max_idx] - 1, numbers[min_idx] + 1
        
    # 최대 최소 인덱스 구해서 차이return
    max_idx, min_idx = min_max(numbers)
    return numbers[max_idx] - numbers[min_idx]

if __name__=="__main__":
    for test_case in range(1, 11):
        N = int(input())
        numbers = list(map(int, input().split()))
        print(f'#{test_case} {flatten(numbers, N)}')
