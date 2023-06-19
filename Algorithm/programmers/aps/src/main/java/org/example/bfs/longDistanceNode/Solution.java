package org.example.bfs.longDistanceNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

    public int solution(int n, int[][] edge) {
        List<Integer>[] adjList = new ArrayList[n + 1];

        for (int i = 0; i <= n; i++)
            adjList[i] = new ArrayList<>();

        int len = edge.length;
        for (int i = 0; i < len; i++) {
            adjList[edge[i][0]].add(edge[i][1]);
            adjList[edge[i][1]].add(edge[i][0]);
        }

        return getCntFarNodes(n, adjList);
    }

    private int getCntFarNodes(int n, List<Integer>[] adjList) {
        int[] visited = new int[n + 1];
        Queue<Integer> q = new LinkedList<>();

        q.add(1);
        visited[1] = 0;

        while (!q.isEmpty()) {
            int now = q.poll();
            List<Integer> connectedNodes = adjList[now];
            for (int node : connectedNodes) {
                if (visited[node] != 0 || node == 1) continue;
                visited[node] = visited[now] + 1;
                q.add(node);
            }
        }

        int longestDistance = -1;
        int countLD = 0;
        for (int distance : visited) {
            if (distance > longestDistance) {
                longestDistance = distance;
                countLD = 1;
            } else if (distance == longestDistance)
                countLD++;
        }
        return countLD;
    }
}