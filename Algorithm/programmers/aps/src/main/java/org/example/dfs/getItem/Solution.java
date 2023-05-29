package org.example.dfs.getItem;

import java.util.*;

/**
 *  로직
 *  0. 사각형을 사이즈를 두배로 늘려서 인접한 모서리끼리 이동하는 경우를 없앤다.
 *  1. 모서리는 1, 내부는 2로 그린다.
 *      1. 그리는 과정에서
 *          이미 내부인 경우는 패스
 *          모서리인 경우, 못가는 방향 지우기
 *  2. dfs
 */
class Solution {
    int MAX_GRID = 104;
    int[][] grid = new int[MAX_GRID][MAX_GRID];
    boolean[][][] directs = new boolean[MAX_GRID][MAX_GRID][4];
    // 0 : 하 , 1 : 우, 2 : 상, 3 : 좌

    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    int answer;

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        answer = Integer.MAX_VALUE;
        for (int[] rec : rectangle)
            drawRectangle(rec);

        boolean[][] visited = new boolean[MAX_GRID][MAX_GRID];
        visited[characterX * 2][characterY * 2] = true;

        dfs(0, visited, characterX * 2, characterY * 2, itemX * 2, itemY * 2);

        return answer / 2;
    }

    private void drawRectangle(int[] r) {
        int frx = r[0] * 2, fry = r[1] * 2, tox = r[2] * 2, toy = r[3] * 2;
        for (int x = frx; x <= tox; x++) {
            for (int y = fry; y <= toy; y++) {
                // 사각형 내부라면 패스
                if (grid[x][y] == 2) continue;
                // 0 : 하 , 1 : 우, 2 : 상, 3 : 좌

                if (x == frx || x == tox || y == fry || y == toy) {
                    // 이미 모서리일 경우 못가는 방향 제거
                    if (grid[x][y] == 1) {
                        if (x == frx)
                            directs[x][y][0] = false;
                        if (x == tox)
                            directs[x][y][2] = false;
                        if (y == fry)
                            directs[x][y][1] = false;
                        if (y == toy)
                            directs[x][y][3] = false;
                    }
                    // 모서리 별 갈 수 있는 방향 표시
                    if (y == fry || y == toy) {
                        directs[x][y][0] = true;
                        directs[x][y][2] = true;
                        // 꼭지점인 경우 못가는 방향 지우기
                        if (x == frx)
                            directs[x][y][2] = false;
                        if (x == tox)
                            directs[x][y][0] = false;
                    }
                    if (x == frx || x == tox) {
                        directs[x][y][1] = true;
                        directs[x][y][3] = true;
                        if (y == fry) {
                            directs[x][y][3] = false;
                        }
                        if (y == toy)
                            directs[x][y][1] = false;
                    }
                    grid[x][y] = 1;
                } else
                    grid[x][y] = 2;
            }
        }
    }

    private void dfs(int depth, boolean[][] visited, int frx, int fry, int tox, int toy) {
        if (frx == tox && fry == toy) {
            answer = Math.min(answer, depth);
        } else {
            int nx, ny;
            for (int i = 0; i < 4; i++) {
                nx = frx + dx[i];
                ny = fry + dy[i];
                if (!canGo(frx, fry, nx, ny, i, visited)) continue;
                visited[nx][ny] = true;
                dfs(depth + 1, visited, nx, ny, tox, toy);
                visited[nx][ny] = false;
            }
        }
    }

    private boolean canGo(int frx, int fry, int nx, int ny, int dir, boolean[][] visited) {
        return grid[nx][ny] == 1 && !visited[nx][ny] && directs[frx][fry][dir];
    }
}