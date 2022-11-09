'''
문자별로 와일드카드가 포함된 문자가 매칭되는 개수가 담긴 배열을 반환

논리
- 이진탐색으로 어떻게 해야 할까
- 정렬 기준을 앞문자부터 정렬과 뒷문자 기준 정렬 두가지 찾는다.
- 문자열 전체로 대소 비교가 가능하다.
- 일단 가사단어 길이마다 배열

result = [3, 2, 4, 1, 0]

답은 맞는데 시간초과

'''
words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']

from bisect import bisect_left, bisect_right


def count_match(arr, min_query, max_query):
<<<<<<< HEAD
    min_idx, max_idx = 0, 1
    length = len(arr)
    fr, to = 0, length

    while fr <= to:
        mid = (to + fr) // 2
        if min_query <= arr[mid] <= max_query:
            for i in range(mid, length):
                if arr[i] > max_query:
                    max_idx = i
                    break
            else:
                max_idx = length

            for i in range(mid, -1, -1):
                if arr[i] < min_query:
                    min_idx = i
                    break
            else:
                min_idx = -1
            break

        elif arr[mid] < min_query:
            fr = mid + 1
        elif arr[mid] > max_query:
            to = mid - 1

    return max_idx - min_idx - 1

arr_suffix = [[] for i in range(10001)]
arr_prefix = [[] for i in range(10001)]

for word in words:
    n = len(word)
    arr_prefix[n].append(word[::-1])
    arr_suffix[n].append(word)

for query in queries:
    res = 0

    if query[-1] == '?' and len(arr_suffix[len(query)]) != 0:
        res = count_match(sorted(arr_suffix[len(query)]), query.replace('?', 'a'), query.replace('?', 'z'))
    elif query[0] == '?' and len(arr_prefix[len(query)]) != 0:
        res = count_match(sorted(arr_prefix[len(query)]), query.replace('?', 'a')[::-1], query.replace('?', 'z')[::-1])
    print(res)
print(arr_prefix)
print(arr_suffix)
=======
    right_index = bisect_right(arr, max_query)
    left_index = bisect_left(arr, min_query)
    return right_index - left_index


def solution(words, queries):
    arr_suffix = [[] for i in range(10001)]
    arr_prefix = [[] for i in range(10001)]

    for word in words:
        n = len(word)
        arr_prefix[n].append(word[::-1])
        arr_suffix[n].append(word)

    for i in range(10001):
        if arr_prefix[i]:
            arr_prefix[i].sort()
        if arr_suffix[i]:
            arr_suffix[i].sort()

    answer = []

    for query in queries:
        res = 0

        if query[-1] == '?':
            res = count_match(sorted(arr_suffix[len(query)]), query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            res = count_match(sorted(arr_prefix[len(query)]), query.replace('?', 'a')[::-1],
                              query.replace('?', 'z')[::-1])

        answer.append(res)

    return answer

>>>>>>> 5b5b4d0ac5f8ef4f4077dae23157524bc2b83fe8
'''
arr_suffix = sorted(words)
arr_prefix = sorted(words, key=lambda word: word[-1::-1])

len_w = len(words)

def cnt_match(mid, n, length, len_w):
    count = 0
    for i in [-1, 1]:
        j = i
        while 0 <= mid + j < len_w:
            if len(words[mid + j]) == n:
                if query[:length] == words[mid + j][:length]:
                    count += 1
                else:
                    break
            j += j
    return count

for query in queries:
    if query[-1] == '?':
        n, length = len(query), query.index('?')
        fr, to = 0, len_w
        cnt = 0

        while fr <= to:
            mid = (to + fr) // 2
            if len(words[mid]) == n and query[:length] == words[mid][:length]:
                cnt += 1
                cnt += cnt_match(mid, n, length, len_w)


                while j < len_w:
                    if len(words[mid + j]) >= n and query[:length] == words[mid + k][:length]:
                        cnt += 1
                        j -= 1

                while k < n and query[:n] == words[mid + k][:n]:
                    cnt += 1
                    k += 1
'''