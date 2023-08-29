# 트리의 순회
## 트리의 모든 노드를 순회
### 트리의 루트가 주어질 때 루트를 방문한 뒤 각 서브 트리를 재귀적으로 방문하는 함수
# 연결리스트
# 노드 수 : 13
# 연결관계 frm- to : 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 1
# 2    3
# 4    5    6
# 7    8 9   10  11
# 12             13

def LKLpreorder(n):
    if n:
        print(n, end=' ') # 전위순회
        # 1 2 4 7 12 3 5 8 9 6 10 11 13

        for i in range(len(LKL[n])):
            LKLpreorder(LKL[n][i])
        # print(n, end=' ') # 후위순회
        # 12 7 4 2 8 9 5 10 13 11 6 3 1 

# 트리의 높이 구하기 
def height(n):
    h = 0
    if not n:
        return 0

    for i in range(len(LKL[n])):
        h = max(h, 1 + height(LKL[n][i]))
    return h


v = int(input())
e = v - 1
LKL = [[] for i in range(v + 1)]
edges = list(map(int, input().split()))

for i in range(0, e * 2, 2):
    LKL[edges[i]].append(edges[i + 1])
# **[[], [2, 3], [4], [5, 6], [7], [8, 9], [10, 11], [12], [], [], [], [13], [], []]**
LKLpreorder(1)

print()
tree_h = height(1) + 1
print(tree_h) # 5
