def selection_sort(arr, n):


    for i in range(n-1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

if __name__=="__main__":
    T = int(input())
    
    for test_case in range(1, T + 1):
        N = int(input())
        numbers = list(map(int, input().split()))

        res = selection_sort(numbers, N)
        result = ''

        for num in res:
            result += str(num) + ' '

        print(f"#{test_case} {result[:-1]}")
