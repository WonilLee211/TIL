package ListPushPull.P2;

import java.util.*;
import java.io.*;

/** 격자 안에서 밀고 당기기/ 삼각형 컨베이어 벨트
 */
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int n, t;
    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); t = Integer.parseInt(st.nextToken());
        int[][] grid = new int[3][n];

        for (int i = 0; i < 3; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++)
                grid[i][j] = Integer.parseInt(st.nextToken());
        }
        int[] temps = new int[3];
        while (t > 0){
            for (int i = 0; i < 3; i++)
                temps[i] = grid[i][n - 1];
            for (int i = n - 2; i > -1; i--){
                for (int j = 0; j < 3; j++)
                    grid[j][i + 1] = grid[j][i];
            }
            for (int i = 1; i <= 3; i++){
                grid[i % 3][0] = temps[i - 1];
            }
            t--;
        }

        for (int i = 0; i < 3; i++){
            for (int num : grid[i])
                bw.append(String.valueOf(num)).append(" ");
            bw.append("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}