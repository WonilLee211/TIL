import sys
sys.stdin = open('input.txt')

'''
양방향 그래프

입력
n, m : 여행지 개수, 여행 계획에 속한 도시의 수 (1 <= n, m < 500)
n * n 행렬 : 여행지 간의 연결정보
    - 1 : 연결
    - 2 : 연결 x
여행 계획에 포함됨 여행지 번호들 : m 개

출력
여행계획이 가능한지 여부 출력
YES or NO

논리
1. 경로 완전 탐색으로 목적지 모두 포함하는 경우가 있는지 확인
2. 목적지 중 하나에서 출발. 
 - dfs로 모든 갈 수 있는 모든 경로에 도달한 후,
 - 경로에 모든 목적지가 포함되어있는지 확인
    - dfs 조건 : 연결된 노드 중에 방문하지 않았고, 목적지에 포함되어있으면 나아가기
'''
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split())) # 여행지 개수, 여행 계획에 속한 도시의 수
matrix = [list(map(int, input().split())) for _ in range(n)] # 연결 정보

places = list(map(int, input().split()))
visited = []

def dfs(fr):
    # 연결된 노드 중에 방문하지 않았고, 목적지에 포함되어있으면 나아가기
    for node, isConnected in enumerate(matrix[fr]):
        if isConnected == 0:
            continue

        if (node + 1) not in visited and (node + 1) in places:
            visited.append(node + 1)
            dfs(node)

dfs(places[0])  # 목적지 중 하나를 시작으로 탐색

if (set(visited) & set(places)) == set(places): # visited : [2, 3, 4]
    print("YES")
else:
    print("NO")

