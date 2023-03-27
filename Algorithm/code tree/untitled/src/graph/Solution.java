package graph;


import java.io.*;
import java.util.*;

/** 방화벽 3개를 추가로 설치 했을 때 방화벽을 제외하고 불이 퍼지지 않는 영역 크기의 최댓값을 출력합니다.
 *  입력 : 각 행에 불이 있는 경우 2, 방화벽이 있는 경우 1, 빈 칸인 경우 0이 입력
 *  출력 : 불이 퍼지지 않는 영역 크기의 최댓값을 출력
 *
 *  로직
 *  1. fires와 walls 인덱스 찾기
 *  2. 벽 세우기
 *      - 0인 값에 벽 3개 세우기
 *  3. dfs로 불마다 전파시키기
 *      - visited 표시
 *      - 불퍼진 개수가 지금보다 커지면 return
 *      - dfs가 끝난 후 불퍼지지 않는 영역 크기 최댓값 업데이트
 *  4. 세운 벽 초기화
 */

public class Solution {
    static int n, m;
    static int maxCnt;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] matrix;
    static ArrayList<Node> emptyPlaces;
    static ArrayList<Integer> selectedIndices = new ArrayList<>();
    static Queue<Node> q = new LinkedList<>();
    static int[][] visited = new int[n][m];
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        matrix = new int[n][m];
        emptyPlaces = new ArrayList<>();
        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                int num = Integer.parseInt(st.nextToken());
                if (num == 0) emptyPlaces.add(new Node(i, j));
                matrix[i][j] = num;
            }
        }
        setThreeWall(0, 0);
        System.out.println(maxCnt);
    }
    private static void setThreeWall(int count, int depth){
        if (count == 3){
            getArea();
            return;
        }
        if (depth == emptyPlaces.size())
            return;

        selectedIndices.add(depth);
        setThreeWall(count + 1, depth + 1);
        selectedIndices.remove(selectedIndices.size() -1);
        setThreeWall(count, depth + 1);
    }
    private static void getArea(){
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        visited = new int[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                visited[i][j] = 0;
                if (matrix[i][j] == 2) {
                    q.add(new Node(i, j));
                    visited[i][j] = 1;
                }
            }
        }
        for (int i = 0; i < selectedIndices.size(); i++){
            int idx = selectedIndices.get(i);
            int r = emptyPlaces.get(idx).r;
            int c = emptyPlaces.get(idx).c;
            matrix[r][c] = 1;
        }
        while(!q.isEmpty()){
            Node fire = q.poll();
            int cr = fire.r;
            int cc = fire.c;

            for (int i = 0; i < 4; i++){
                int nr = cr + dx[i];
                int nc = cc + dy[i];
                if (canGo(nr, nc)){
                    q.add(new Node(nr, nc));
                    visited[nr][nc] = 1;
                }
            }
        }

        int emptyCnt = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (visited[i][j] == 0 && matrix[i][j] == 0) emptyCnt++;
            }
        }
        maxCnt = Math.max(emptyCnt, maxCnt);

        for (int i = 0; i < selectedIndices.size(); i++){
            int idx = selectedIndices.get(i);
            int r = emptyPlaces.get(idx).r;
            int c = emptyPlaces.get(idx).c;
            matrix[r][c] = 0;
        }
    }
    private static boolean canGo(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < m && visited[r][c] == 0 && matrix[r][c] == 0;
    }

    private static class Node{
        private int r;
        private int c;

        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}
