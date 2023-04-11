package brute_force;

import java.util.*;
import java.io.*;
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int ans, temp;
    static int[][] grid;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        int n = Integer.parseInt(br.readLine());
        ans = 0;
        grid = new int[n][n];

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n-2; i++){
            for (int j = 0; j < n-2; j++){
                ans = Math.max(ans, sumThreeMatrix(i, j));
            }
        }
        System.out.println(ans);
    }

    private static int sumThreeMatrix(int r, int c){
        temp = 0;
        for (int dr = 0; dr < 3; dr++){
            for (int dc = 0; dc < 3; dc++){
                temp += grid[r + dr][c + dc];
            }
        }
        return temp;
    }
}