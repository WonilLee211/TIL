package brute_force.bruteForce_searchFullRowColumn;

import java.util.*;
import java.io.*;

/** 행복 수열 찾기
 * 문제 : m개의 동일한 원소가 연속하게 나타난 행 또는 열 세기
 * 로직
 *  1. 데이터 전처리
 *  2.
 */
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m, countColumn, countRow, ans;
    static int[][] grid;
    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][n];
        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ans = 0;

        findHappiness();
        System.out.println(ans);
    }

    private static void findHappiness(){

        for (int i = 0; i < n; i++){
            countRow = 1;
            countColumn = 1;
            for (int j = 1; j < n; j++){
                if (countRow < m){
                    if (Objects.equals(grid[i][j], grid[i][j - 1])) countRow++;
                    else {
                        countRow = 1;
                    }
                }
                if (countColumn < m){
                    if (Objects.equals(grid[j][i], grid[j-1][i])) countColumn++;
                    else {
                        countColumn = 1;
                    }
                }
            }
            if (countRow >= m) ans++;
            if (countColumn >= m) ans++;

        }
    }
}