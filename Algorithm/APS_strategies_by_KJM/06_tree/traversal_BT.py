'''
문제 : 트리 순회 순서 변경
- 전위순회와 중위순회 결과를 입력받을 때 후위 순회를 출력하기

풀이
- 루트 : 전위 순회에서 가장 먼저 방문되는 곳
    - 왼쪽 서브트리 : 중위 순회에서 루트보다 일찍 방문한 곳
    - 오른쪽 서브트리 : 중위 순회에서 루트보다 늦게 방문한 곳
- 리스트들을 서브트리로 슬라이싱하고 후위순회
'''
def PrintPostOrder(preorder, inorder):
    # 트리에 포함된 노드의 수
    n = len(preorder)
    # 기저 상태
    if not n: return
    root = preorder[0]
    # 왼쪽 서브트리 크기
    L = inorder.index(root)

    # 후위순회
    PrintPostOrder(preorder[1:L + 1], inorder[:L])
    PrintPostOrder(preorder[L + 1:], inorder[L + 1:])
    print(root, end = ' ')

import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):

    v = int(input())
    e = v - 1
    pre_arr = list(map(int, input().split()))
    in_arr = list(map(int, input().split()))
    PrintPostOrder(pre_arr, in_arr)
