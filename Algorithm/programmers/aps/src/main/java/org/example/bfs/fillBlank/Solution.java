package org.example.bfs.fillBlank;

import java.util.*;

/**
 * 로직
 * 필요한 변수 및 리스트 초기화
 * 테이블의 값 전환 (1을 0으로, 0을 1로 변경)
 * 테이블로부터 블록 추출
 * 보드로부터 빈 공간 추출
 * 일치하는 블록 개수 계산
 * 결과 반환
 */
class Solution {
    // 상하좌우 이동을 위한 배열
    int[] dr = {0, 0, 1, -1};
    int[] dc = {1, -1, 0, 0};

    int n, answer;
    List<List<Point>> blockInTable = new ArrayList<>();  // 게임 테이블의 블록들을 저장하는 리스트
    List<List<Point>> blockInBoard = new ArrayList<>();  // 게임 보드의 빈 공간들을 저장하는 리스트
    boolean[][] visitedTable;  // 게임 테이블의 블록 방문 여부를 저장하는 배열
    boolean[][] visitedBoard;  // 게임 보드의 빈 공간 방문 여부를 저장하는 배열
    boolean[] usedBlockInTable;  // 테이블의 블록 사용 여부를 저장하는 배열

    class Point implements Comparable<Point> {
        int r;
        int c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public int compareTo(Point p) {
            int res = this.r - p.r;
            if (res == 0)
                res = this.c - p.c;
            return res;
        }

        public String toString() {
            return "( " + this.r + ", " + this.c + " )";
        }

        public void rotate() {
            int temp = this.r;
            this.r = this.c;
            this.c = -temp;
        }

        public void replacePoint(int stR, int stC) {
            this.r -= stR;
            this.c -= stC;
        }
    }

    public int solution(int[][] game_board, int[][] table) {
        answer = 0;
        n = game_board.length;
        visitedTable = new boolean[n][n];
        visitedBoard = new boolean[n][n];
        // 테이블의 1을 0으로, 0을 1로 변경
        switchTableValue(table);
        // 테이블로부터 블록 추출
        extractBlockFrom(table, visitedTable, blockInTable);
        // 보드로부터 빈 공간 추출
        extractBlockFrom(game_board, visitedBoard, blockInBoard);
        // 일치하는 블록 개수 계산
        usedBlockInTable = new boolean[blockInTable.size()];
        countMatch();

        return answer;
    }

    private void switchTableValue(int[][] table) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (table[i][j] == 1)
                    table[i][j] = 0;
                else
                    table[i][j] = 1;
            }
        }
    }

    private void extractBlockFrom(int[][] arr, boolean[][] visited, List<List<Point>> list) {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                // 빈 공간인 경우, 방문하지 않았다면 bfs 탐색을 통해 블록 추출
                if (arr[i][j] == 0 && !visited[i][j]) list.add(bfs(i, j, arr, visited));
    }

    private List<Point> bfs(int r, int c, int[][] arr, boolean[][] visited) {
        List<Point> block = new ArrayList<>();  // 블록 좌표를 저장하는 리스트
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(r, c));
        block.add(new Point(0, 0));  // 블록의 시작점을 원점으로 설정
        visited[r][c] = true;
        int nr, nc;

        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                nr = p.r + dr[i];
                nc = p.c + dc[i];
                // 배열 범위 내에 있고, 빈 공간이면서 방문하지 않았다면 블록에 추가하고 큐에 삽입
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && arr[nr][nc] == 0 && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    block.add(new Point(nr - r, nc - c));  // 상대 좌표로 변환하여 저장
                    q.add(new Point(nr, nc));
                }
            }
        }
        Collections.sort(block);  // 블록 좌표를 정렬
        return block;
    }

    private void countMatch() {
        int m = blockInTable.size();  // 테이블의 블록 개수

        for (List<Point> bBoard : blockInBoard) {
            for (int i = 0; i < m; i++) {
                // 빈 공간의 크기가 테이블의 블록과 다르거나 이미 사용한 블록인 경우, 다음으로 넘어감
                if (bBoard.size() != blockInTable.get(i).size() || usedBlockInTable[i]) continue;
                if (equalBoth(bBoard, blockInTable.get(i))) {
                    usedBlockInTable[i] = true;
                    answer += blockInTable.get(i).size();  // 일치하는 블록 개수를 더함
                    break;
                }
            }
        }
    }

    private boolean equalBoth(List<Point> bBoard, List<Point> bTable) {
        int len = bBoard.size();
        // 90도씩 회전하며 두 리스트가 일치하는지 확인
        for (int i = 0; i < 4; i++) {
            boolean isMatchAll = true;
            int j;
            for (j = 0; j < len; j++) {
                if (bBoard.get(j).r != bTable.get(j).r || bBoard.get(j).c != bTable.get(j).c) {
                    isMatchAll = false;
                    break;
                }
            }
            if (isMatchAll)
                return true;
            else {
                // 블록을 회전시키고 좌표를 재배치하여 다시 확인
                for (int k = 0; k < len; k++)
                    bTable.get(k).rotate();
                Collections.sort(bTable);
                int stR = bTable.get(0).r;
                int stC = bTable.get(0).c;
                for (int k = 0; k < len; k++)
                    bTable.get(k).replacePoint(stR, stC);
            }
        }
        return false;
    }
}