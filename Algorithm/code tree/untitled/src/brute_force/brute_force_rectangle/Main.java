package brute_force.brute_force_rectangle;

import java.util.*;
import java.io.*;
/*
기울어진 직사각형을 따라서 더한 값의 총합이 가장 큰 값 출력

로직
1. 모든 점에 대해서 기울어진 직사각형을 그린다.
2. 한 점에 대해서
    현재 위치에서 그릴 수 있는 모든 높이와 너비를 구한다.
    해당 높이와 너비에 따라가며 누적값을 구한다.
3. 갈 수 없는 범위는 중간에 0을 return한다.
*/

public class Main {
    public static final int DIR_NUM = 4;
    public static final int MAX_N = 20;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[] dr = new int[]{1, -1, -1, 1};
    static int[] dc = new int[]{-1, -1, 1, 1};
    static int[][] grid = new int[MAX_N][MAX_N];
    static int n, ans, nr, nc;

    public static void main(String[] args) throws Exception {
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                for (int w = 1; w <= n; w++){
                    for (int h = 1; h <= n; h++){
                        ans = Math.max(ans, findMaxRectangle(i, j, w, h));
                    }
                }
            }
        }
        System.out.println(ans);
    }

    private static int findMaxRectangle(int r, int c, int w, int h){
        int[] wh = new int[]{w, h, w, h};
        int acc = 0;

        for (int d = 0; d < DIR_NUM; d++){
            for (int m = 0; m < wh[d]; m++){
                r += dr[d]; c += dc[d];
                if (!canGo(r, c)){
                    return 0;
                }
                acc += grid[r][c];
            }
        }
        return acc;
    }
    private static boolean canGo(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < n;
    }

}