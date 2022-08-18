
'''
 A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하라
'''

def dfs(start):
    visited[start] = 1

    if visited[99]:
        return

    for node in adj_dict[start]:
        if not visited[node]:
            dfs(node)

if __name__ == '__main__':
    start, end = 0, 99

    for tc in range(1, 11):
        testcase, E = map(int, input().split())

        # 어떤 정점이 들어올지 몰라서 다 만들어 놓기
        adj_dict = {i : [] for i in range(100)}
        visited = {i : 0 for i in range(100)}

        arr = list(map(int, input().split()))
        M = len(arr)

        for i in range(0, M, 2):
            adj_dict[arr[i]].append(arr[i+1])

        dfs(0)
        if visited[99]:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')