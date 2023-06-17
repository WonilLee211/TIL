package org.example.implementation.divideNetwork;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        List<Integer>[] net = new ArrayList[n + 1];

        // 각 노드별 연결 리스트 초기화
        for (int i = 0; i <= n; i++) {
            net[i] = new ArrayList<>();
        }

        // 연결 리스트 생성
        for (int i = 0; i < n - 1; i++) {
            net[wires[i][0]].add(wires[i][1]);
            net[wires[i][1]].add(wires[i][0]);
        }

        // 하나씩 지우고 탐색
        for (int i = 0; i < n - 1; i++) {
            int node1 = wires[i][0];
            int node2 = wires[i][1];

            net[node1].remove((Integer) node2);
            net[node2].remove((Integer) node1);

            answer = Math.min(answer, getDiff(net, n));

            net[node1].add(node2);
            net[node2].add(node1);
        }
        return answer;
    }

    private int getDiff(List<Integer>[] net, int n) {
        for (int i = 1; i <= n; i++)
            if (!net[i].isEmpty())
                return diff(net, n, i);
        return 1;
    }

    private int diff(List<Integer>[] net, int n, int i) {
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> q = new LinkedList<>();

        q.add(i);
        visited[i] = true;
        int cnt = 1;

        while (!q.isEmpty()) {
            int fr = q.poll();

            for (int to : net[fr]) {
                if (visited[to]) continue;
                q.add(to);
                visited[to] = true;
                cnt++;
            }
        }
        return Math.abs(n - 2 * cnt);
    }
}
