## -1. 단순한 순열 생성 방법

# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i1 != i2:
#             for i3 in range(1,4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)

'''
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''

# ## -2. 재귀호출을 통한 순열 생성
# def nPr(r, depth = 0):
#     if depth == r:
#         print(arr[:r])
#     else:
#         for i in range(depth, n):
#             arr[i], arr[depth] = arr[depth], arr[i]
#             nPr(r, depth + 1)
#             arr[i], arr[depth] = arr[depth], arr[i]


# arr = [1, 2, 3]
# n = len(arr)
# nPr(2)
# '''
# [1, 2]
# [1, 3]
# [2, 1]
# [2, 3]
# [3, 2]
# [3, 1]
# '''

## -4.사용 여부 배열을 이용한 순열
# p[] : 순열을 저장하는 배열, arr[i] : 순열을 만드는데 사용할 숫자 배열
# n = 원소의 개수, i = 선택된 원소의 수
# used[N-1] : 사용 여부, p : 결과 저장 배열

def perm(i):
    if i == n:
        print(p)
    else:
        for j in range(n):
            if not used[j]:
                used[j] = 1
                p[i] = a[j]
                perm(i+1)
                used[j] = 0

n = 3
a =[i for i in range(1, n + 1)]
used = [0] * n
p = [0] * n
perm(0)
'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''