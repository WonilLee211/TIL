package brute_force_sum_pattern;
import java.util.*;
import java.io.*;
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] board, dr1, dc1;
    static int[] dr2, dc2;
    static int n, m, ans;
    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ans = 0;
        board = new int[n][m];
        dr1 = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        dc1 = new int[][]{{0, -1}, {-1, 0}, {0, -1}, {-1, 0}, {0, 1}, {1, 0}, {0, 1}, {1, 0}};
        dr2 = new int[]{1, 0, 0, -1};
        dc2 = new int[]{0, 1, -1, 0};

        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int r=0; r<n; r++){
            for (int c=0; c<m; c++){
                sumSquare(r, c);
                sumBar(r, c);
            }
        }
        System.out.println(ans);

    }

    private static void sumSquare(int r, int c){
        int nr, nc, temp;
        for (int i = 0; i < 8; i++){
            nr = r;
            nc = c;
            temp = board[r][c];
            for (int j = 0; j < 2; j++){
                nr = nr + dr1[i][j];
                nc = nc + dc1[i][j];
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                    temp = 0;
                    break;
                }
                temp += board[nr][nc];
            }
            ans = Math.max(ans, temp);
        }
    }

    private static void sumBar(int r, int c){
        int nr , nc, temp;
        for (int i = 0; i < 4; i++){
            nr = r;
            nc = c;
            temp = board[r][c];
            for (int j = 0; j < 2; j++){
                nr = nr + dr2[i];
                nc = nc + dc2[i];
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                    temp = 0;
                    break;
                }
                temp += board[nr][nc];
            }
            ans = Math.max(ans, temp);
        }
    }
}