package brute_force.brute_force_rectangle2;

import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m;
    static int[][] grid;
    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); m = Integer.parseInt(st.nextToken());
        grid = new int[n][m];

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) grid[i][j] = Integer.parseInt(st.nextToken());
        }
        int ans = 0;
        int temp = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                for (int k = i; k < n; k++){
                    for (int l = j; l < m; l++){
                        if (isNegative(i, j, k, l)) continue;
                        ans = Math.max(ans, findMaxRectangle(i, j, k, l));
                    }
                }
            }
        }
        if (ans == 0) System.out.println(-1);
        else System.out.println(ans);
    }
    private static boolean isNegative(int fr, int fc, int tr, int tc){
        for (int i = fr; i <= tr; i++)
            for (int j = fc; j <= tc; j++)
                if (grid[i][j] <= 0) return true;
        return false;
    }

    private static int findMaxRectangle(int fr, int fc, int tr, int tc){
        return (tc - fc + 1) * (tr - fr + 1);
    }
}