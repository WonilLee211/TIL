'''
1부터 12까지의 숫자를 원소로 가진 집합 A
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 
원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오
'''
def sum_subset(arr, n, k):
    result = 0

    # 이진 연산자를 이용한 부분집합 구하기
    for i in range(1 << 12):
        temp = []

        for j in range(12):
            if i & (1 << j):
                temp.append(arr[j])

        if len(temp) == n:
            temp_total = 0
            for x in temp:
                temp_total += x

            if temp_total == k:
                result += 1

    return result

if __name__=="__main__":
    T = int(input())
    
    set_ = [i for i in range(1, 13)]

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        print(f"#{test_case} {sum_subset(set_, N, K)}")
