import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_idx = 0
diff_arr = []
result = 0

if k ==1 :
    result = max(arr)
else:
    for i in range(n - k):
        diff_arr.append(arr[i+k] - arr[i])


    max_acc = acc = 0

    for i in range(n - k):
        acc += diff_arr[i]
        if acc > max_acc:
            max_acc = acc
            max_idx = i+1

    for i in range(k):
        result += arr[i + max_idx]

print(result)