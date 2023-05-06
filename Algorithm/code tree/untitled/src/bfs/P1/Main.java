package bfs.P1;

import java.util.*;
import java.io.*;

public class Main {
    static int MAX_NM = 100;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, m, tX, tY;
    static int[][] grid = new int[MAX_NM][MAX_NM];
    static int[] dx = new int[]{0, 0, -1, 1};
    static int[] dy = new int[]{-1, 1, 0, 0};
    static boolean[][] visited = new boolean[MAX_NM][MAX_NM];
    static Queue<Pair> q = new LinkedList<>();
    static StringTokenizer st;
    static class Pair {
        int x;
        int y;
        public Pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        tY = n - 1;
        tX = m - 1;

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
                visited[i][j] = false;
            }
        }
        System.out.println(bfs());
    }
    private static int bfs(){
        int newX, newY;
        q.add(new Pair(0, 0));
        visited[0][0] = true;
        while(!q.isEmpty()){
            Pair p = q.poll();
            for (int i = 0; i < 4; i++){
                newX = p.x + dx[i];
                newY = p.y + dy[i];
                if(!canGo(newX, newY)) continue;
                if (Objects.equals(newX, tX) && Objects.equals(newY, tY)) return 1;
                visited[newY][newX] = true;
                q.add(new Pair(newX, newY));
            }
        }
        return 0;
    }
    private static boolean canGo(int x, int y){
        return y >= 0 && y < n && x >= 0 && x < m && !visited[y][x] && grid[y][x] == 1;
    }
}