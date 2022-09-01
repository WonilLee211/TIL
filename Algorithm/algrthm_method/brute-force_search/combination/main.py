import itertools

data = [1, 2, 3]

for i in itertools.combinations(data, 2):
    print(list(i), end=' ')
 # [1, 2] [1, 3] [2, 3]
'''
def comb(arr, n):
    result = []

    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)

    return result

arr = [1, 2, 3]
print(comb(arr, 1)) # [[1], [2], [3]]
print(comb(arr, 2)) # [[1, 2], [1, 3], [2, 3]]
print(comb(arr, 3)) # [[1, 2, 3]]
'''



''' (수정중)
def combination(n, r, j, c=[]):
    if r == 0:
        print(c)

    else:
        for i in range(j, 1 + n):
            if c.count(i) == 0 and i > max(c):
                c.append(i)
                combination(n, r-1, j + 1, c)
                c.remove(i)

combination(4, 2, 1)
'''