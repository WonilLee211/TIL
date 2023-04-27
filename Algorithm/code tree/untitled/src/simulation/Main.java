package simulation_DFS;
import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

/** 배운 점
 *  1. for loof문에서 new int[][]를 하니 메모리 초과가 났다.
 *  초기화하는 메서드를 사용해서 배열 값을 초기화하는 방법으로 리펙토링하여 memory 소모를 최소화했다.
 */

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] dr = new int[]{1, -1, 0, 0};
    static int[] dc = new int[]{0, 0, -1, 1};
    static int maxValue, sumOfBlocks, cr, cc, n, m;
    static int[][] visited, board;
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maxValue = 0;
        board = new int[n][m];

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        visited = new int[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                checkException(i, j);
                sumOfBlocks = board[i][j];
                cr = i; cc = j;
                visited[i][j] = 1;
                dfs(0, i, j);
                initializeVisited();
            }
        }
        System.out.println(maxValue);
    }
    private static void checkException(int r, int c){
        for (int i = 0; i < 4; i++){
            int sumOfException = board[r][c];
            for (int j = 0; j < 4; j++){
                if (i == j) continue;
                int nr = r + dr[j];
                int nc = c + dc[j];
                if (!canGo(nr, nc)) break;
                sumOfException += board[nr][nc];
            }
            maxValue = Math.max(maxValue, sumOfException);
        }
    }

    private static void dfs(int depth, int r, int c){
        if (depth == 3){
            maxValue = Math.max(maxValue, sumOfBlocks);
            return;
        }

        for (int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (canGo(nr, nc)){
                visited[nr][nc] = 1;
                sumOfBlocks += board[nr][nc];
                dfs(depth + 1, nr, nc);
                sumOfBlocks -= board[nr][nc];
                visited[nr][nc] = 0;
            }
        }
    }
    private static boolean canGo(int i, int j){
        return i >= 0 && i < n && j >= 0 && j < m && visited[i][j] != 1;
    }
    private static void initializeVisited(){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                visited[i][j] = 0;
            }
        }
    }

}