import sys
sys.stdin = open("input.txt")

'''
가능한 한 최소의 수의 얼리 아답터를 확보하여 모든 사람이 이 아이디어를 받아들이게 하는  문제는 매우 중요하다. 
얼리 아답터가 아닌 사람들은 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들인다.
친구 관계 그래프가 트리인 경우, 즉 모든 두 정점 사이에 이들을 잇는 경로가 존재하면서 사이클이 존재하지 않는 경우만 고려한다
모든 개인이 새로운 아이디어를 수용하기 위하여 필요한 최소 얼리 어답터의 수를 구하는 프로그램을 작성하시오.

각 노드별로 자신이 얼리일때 아닐때
0: 얼리일 때 자식이 일반인일 경우 최소 얼리 어답터 수 VS 자식이 얼리이 경우 최소 얼리 어답터 수
1: 일반일 때 자식이 얼리일 경우 최소 얼리 어답터 수

'''
import sys
sys.setrecursionlimit(int((1e6)))
input = sys.stdin.readline

n = int(input())

adjList = [[] for _ in range(n + 1)]
dp = [[0, 0] for i in range(n + 1)]
visited = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

def count_early_adapter(node):
    visited[node] = 1
    dp[node][0] = 1

    for child in adjList[node]:
        if visited[child]:
            continue

        count_early_adapter(child)
        dp[node][0] += min(dp[child][0], dp[child][1])
        dp[node][1] += dp[child][0]

count_early_adapter(1)
print(min(dp[1]))
