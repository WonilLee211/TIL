package org.example.implementation.rectangleSnail;

import java.util.Objects;

class Solution {
    int[] dr = new int[]{1, 0, -1};
    int[] dc = new int[]{0, 1, -1};

    public int[] solution(int n) {
        if (n == 1)
            return new int[]{1};

        int[] answer = new int[n * (n + 1) / 2];
        int[][] rectangle = new int[n][n];

        insertNumberIn(rectangle, 0, 0);

        int idx = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < i + 1; j++)
                answer[idx++] = rectangle[i][j];

        return answer;
    }

    private void insertNumberIn(int[][] rec, int r, int c) {
        int num = 1;
        int d = 0;
        rec[r][c] = num;
        int nr = r + dr[d];
        int nc = c + dc[d];

        while (true) {
            rec[nr][nc] = ++num;
            r = nr;
            c = nc;
            nr = r + dr[d];
            nc = c + dc[d];
            if (!canGo(rec, nr, nc)) {
                d = (d + 1) % 3;
                nr = r + dr[d];
                nc = c + dc[d];
                if (!canGo(rec, nr, nc))
                    return;
            }
        }
    }

    private boolean canGo(int[][] rec, int r, int c) {
        return r >= 0 && r < rec.length && c >= 0 && c < rec.length && Objects.equals(rec[r][c], 0);
    }
}