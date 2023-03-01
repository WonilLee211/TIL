package detectBoom;

import java.io.*;
import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;

public class Solution {
    static int T, tc, N, ans;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static String[][] board;
    static Queue<int[]> q;
    static final int[] dr = {1, 0, -1, 0, 1, 1, -1, -1}, dc = {0, 1, 0, -1, -1, 1, 1, -1};
    public static void main(String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());

        for (tc =1; tc <= T; tc++){
            bw.append("#").append(String.valueOf(tc)).append(" ");
            N = Integer.parseInt(br.readLine());
            board = new String[N][N];

            for (int i = 0; i < N; i++){
                String st = br.readLine();
                for (int j = 0; j < N; j++) board[i][j] = String.valueOf(st.charAt(j));
            }
            ans = 0;
            avoidBoom();

            bw.append(String.valueOf(ans));
            bw.write("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }

    public static void avoidBoom(){

        for (int i = 0; i < N; i ++){
            for (int j = 0; j < N; j++){
                if (!Objects.equals(board[i][j], ".")) continue;
                if (isZero(i, j)) {
                    click(i, j);
                    ans++;
                }
            }
        }

        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if (Objects.equals(board[i][j], ".")) ans++;
            }
        }
    }

    public static void click(int r, int c){
        q = new LinkedList<>();
        q.add(new int[]{r, c});
        while (!q.isEmpty()){
            int[] now = q.poll();
            board[now[0]][now[1]]= "0";
            for (int i = 0; i < 8; i++){
                int nr = now[0] + dr[i];
                int nc = now[1] + dc[i];
                if ( nr < 0 || nr >= N || nc < 0 || nc >= N || !Objects.equals(board[nr][nc], ".")) continue;
                if (isZero(nr, nc)) q.add(new int[]{nr, nc});
                board[nr][nc] = "0";
            }
        }
    }

    public static boolean isZero(int r, int c){
        for (int i = 0; i < 8; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (0 <= nr && nr < N && 0 <= nc && nc < N && Objects.equals(board[nr][nc], "*")) return false;
        }
        return true;
    }
}
