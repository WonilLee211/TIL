package org.example.implementation.fatigue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int solution(int k, int[][] dungeons) {
        List<int[]> cases = generatePermutations(dungeons.length);
        return findMaxTourCount(k, dungeons, cases);
    }

    private List<int[]> generatePermutations(int length) {
        List<int[]> permutations = new ArrayList<>();
        boolean[] visited = new boolean[length];
        int[] current = new int[length];
        generatePermutationsHelper(permutations, current, visited, 0);
        return permutations;
    }

    private void generatePermutationsHelper(List<int[]> permutations, int[] current, boolean[] visited, int depth) {
        if (depth == current.length) {
            permutations.add(Arrays.copyOf(current, current.length));
            return;
        }
        for (int i = 0; i < current.length; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            current[depth] = i;
            generatePermutationsHelper(permutations, current, visited, depth + 1);
            visited[i] = false;
        }
    }

    private int findMaxTourCount(int k, int[][] dungeons, List<int[]> cases) {
        int maxTourCount = 0;
        for (int[] idxs : cases) {
            int count = 0;
            int K = k;
            for (int idx : idxs) {
                if (K >= dungeons[idx][0]) {
                    K -= dungeons[idx][1];
                    count++;
                } else {
                    break;
                }
            }
            maxTourCount = Math.max(maxTourCount, count);
        }
        return maxTourCount;
    }
}
