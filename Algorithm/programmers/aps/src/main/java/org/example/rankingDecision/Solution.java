package org.example.rankingDecision;

import java.util.Arrays;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] resTable = new int[n + 1][n + 1];

        for (int[] r : results) {
            resTable[r[0]][r[1]] = 1;
            resTable[r[1]][r[0]] = -1;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                for (int k = 1; k <= n; k++) {
                    if (resTable[j][k] != 0) continue;
                    if (resTable[j][i] == 1 && resTable[i][k] == 1)
                        resTable[j][k] = 1;
                    else if (resTable[j][i] == -1 && resTable[i][k] == -1)
                        resTable[j][k] = -1;
                }
            }
        }
        for (int[] res : resTable) {
            System.out.println(Arrays.toString(res));
        }
        int cnt;
        for (int i = 1; i <= n; i++) {
            cnt = 0;
            for (int j = 1; j <= n; j++) {
                if (resTable[i][j] == 0)
                    cnt++;
            }
            if (cnt == 1)
                answer++;
        }
        return answer;
    }
}
