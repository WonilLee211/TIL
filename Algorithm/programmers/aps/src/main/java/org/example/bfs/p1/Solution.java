package org.example.bfs.p1;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 로직
 * 1. n개에 대해서 연결되어 있는 점들을 bfs로 탐색
 * 2. 한점에서 연결된 모든 점을 방문하면서 visited를 찍음
 * 3. 다 방문했으면 방문하지 않은 점 하를 찾아서 다시 bfs 돌림
 * 4. 방문하지 않은 점이 없을 때까지
 */

class Solution {
    int N;
    int[] visited;
    Queue<Integer> q = new LinkedList<>();

    public int solution(int n, int[][] computers) {
        N = n;
        visited = new int[N];

        for (int i = 0; i < n; i++)
            visited[i] = 0;

        int answer = 0;
        int node;
        while (true) {
            node = -1;
            for (int i = 0; i < n; i++) {
                if (visited[i] == 0) {
                    node = i;
                    break;
                }
            }
            if (node == -1) break;
            bfs(node, ++answer, computers);
        }
        return answer;
    }

    private void bfs(int node, int cnt, int[][] computers) {
        q.add(node);
        visited[node] = cnt;
        int p;
        while (!q.isEmpty()) {
            p = q.poll();
            for (int i = 0; i < N; i++) {
                if (computers[p][i] != 1 || visited[i] != 0) continue;
                visited[i] = cnt;
                q.add(i);

            }
        }
    }
}