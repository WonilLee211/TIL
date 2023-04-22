package ListPushPull.P1;

import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int n, t;
    static int[][] grid;

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); t = Integer.parseInt(st.nextToken());
        grid = new int[2][n];

        for (int i = 0; i < 2; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++)
                grid[i][j] = Integer.parseInt(st.nextToken());
        }
        int topRight, bottomRight;
        while(t > 0){
            topRight = grid[0][n - 1]; bottomRight = grid[1][n -1];
            for (int i = n - 2; i > -1; i--){
                grid[0][i + 1] = grid[0][i];
                grid[1][i + 1] = grid[1][i];
            }
            grid[1][0] = topRight;
            grid[0][0] = bottomRight;
            t--;
        }
        for (int i = 0; i < 2; i++){
            for (int num : grid[i]){
                bw.append(String.valueOf(num)).append(" ");
            }
            bw.append("\n");
        }
        bw.flush();
        br.close(); bw.close();
    }
}