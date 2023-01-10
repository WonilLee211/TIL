import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

def my_shiftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap_idx.pop(heap[pos])
            heap_idx[parent] = pos
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap_idx.pop(heap[pos])
    heap_idx[newitem] = pos
    heap[pos] = newitem

def my_heappush(heap, item):
    size = len(heap)
    heap_idx[item] = size
    heap.append(item)
    my_shiftdown(heap, 1, size)

def my_shiftup(heap, pos):
    endpos = len(heap)
    startpos = pos # 최상단 인덱스 저장
    newitem = heap[pos]

    childpos = 2 * pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap_idx.pop(heap[pos])
        heap_idx[heap[childpos]] = pos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1

    heap_idx.pop(heap[pos])
    heap_idx[newitem] = pos
    heap[pos] = newitem
    my_shiftdown(heap, startpos, pos) # pop됐던 newitem 자리 찾아주기
def my_heappop(heap):
    lastitem = heap.pop()

    if heap:
        returnitem = heap[1]
        heap_idx.pop(heap[1])
        heap[lastitem] = 1
        heap[1] = lastitem
        my_shiftup(heap, 1)
        return returnitem
    return lastitem

n = int(input())
arr = [0] + list(map(int, input().split()))

m = int(input()) # 쿼리 수

heap = [0] + [arr[i] for i in range(1, n + 1)]
heap_idx = {}
for i in range(1, n + 1):
    heap_idx[arr[i]] = i

for i in range(m):
    query = list(map(int, input().split()))

    if query[0] == 1: # Ai를 v로 바꾼다.
        heap[heap_idx[arr[query[1]]]] = query[2]
        arr[query[1]] = query[2]

    elif query[0] == 2: # heap.pop() -> heap.push()
        min_v = my_heappop(heap)
        print(heap_idx[min_v])
        my_heappush(heap, min_v)
