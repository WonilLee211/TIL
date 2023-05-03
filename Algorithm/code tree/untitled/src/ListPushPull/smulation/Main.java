package ListPushPull.smulation;

import java.util.*;
import java.io.*;
/*
바람이 불면 하나의 행 또는 열이 밀린다.
밀린 후 주변 행열에 값이 겹친다면 반대방향으로 해당 행  또는 열이 밀린다.
겹치는 수가 없을 경우 전파가 끝난다.

로직
1. 바람 정보에 따라 행 또는 열을 밀어낸다.
2.
*/
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m, q;
    static int SHIFT_RIGHT = 1;
    static int SHIFT_LEFT = -1;
    static int[][] grid;

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());
        grid = new int[n + 1][m + 1];

        for (int i = 1; i <= n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++)
                grid[i][j] = Integer.parseInt(st.nextToken());
        }
        int row;
        for (int i = 0; i < q; i++){
            st = new StringTokenizer(br.readLine());
            row = Integer.parseInt(st.nextToken());
            simulate(row, st.nextToken().charAt(0) == 'L' ? SHIFT_RIGHT : SHIFT_LEFT);
        }
        for(int r = 1; r <= n; r++) {
            for(int c = 1; c <= m; c++)
                System.out.print(grid[r][c] + " ");
            System.out.println();
        }
    }


    private static void simulate(int row, int startDir){
        // 1. 바람이 처음 불어온 향의 숫자를 밀어준다.
        shift(row, startDir);
        // 2. 바람이 부른 방향을 바꾼다.
        startDir = flip(startDir);
        // 3. 이동한 후 위 행과 값이 겹치는 요소가 있는지 확인
        for (int r = row, dir = startDir; r >= 2; r--){
            // 4. 있다면 쉬프트하고 방향 바꾸기
            if (hasSameNumber(r, r -1)){
                shift(r - 1, dir);
                dir = flip(dir);
            }
            else break;
        }
        // 4. 이동한 후 아래 행과 값이 겹치는 요소가 있는지 확인
        for (int r = row, dir = startDir; r <= n - 1; r++){
            // 4. 있다면 쉬프트하고 방향 바꾸기
            if (hasSameNumber(r, r + 1)){
                shift(r + 1, dir);
                dir = flip(dir);
            }
            else break;
        }
    }

    private static boolean hasSameNumber(int row1, int row2){
        for (int c = 1; c <= m; c++){
            if (grid[row1][c] == grid[row2][c]) return true;
        }
        return false;
    }

    private static int flip(int dir){
        return dir == SHIFT_LEFT ? SHIFT_RIGHT : SHIFT_LEFT;
    }

    private static void shift(int row, int startDir){
        int temp;
        if (startDir == SHIFT_RIGHT){
            temp = grid[row][m];
            for (int c = m; c >= 2; c--)
                grid[row][c] = grid[row][c - 1];
            grid[row][1] = temp;
        }
        else{
            temp = grid[row][1];
            for (int c = 1; c <= m -1; c++)
                grid[row][c] = grid[row][c + 1];
            grid[row][m] = temp;
        }

    }
}