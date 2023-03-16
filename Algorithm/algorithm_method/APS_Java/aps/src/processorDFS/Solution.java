package processorDFS;


import java.io.*;
import java.util.*;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int T, N, M, minLength, maxConnection, visited;
    static final int[] dr = {1, 0, -1, 0}, dc = {0, 1, 0, -1};
    static int[][] map;
    static List<int[]> coreIdx;
    public static void main(String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());
        int tc;
        for (tc = 1; tc <= T; tc++){
            bw.append("#").append(String.valueOf(tc)).append(" ");
            N = Integer.parseInt(br.readLine());
            map = new int[N][N];
            coreIdx = new ArrayList<>();
            minLength = maxConnection = 0;

            for (int i = 0; i < N; i++){
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++){
                    int core = Integer.parseInt(st.nextToken());
                    map[i][j] = core;
//                    if (i == 0 || j == 0 || i == N - 1 || j == N - 1) continue;
                    if (Objects.equals(core, 1)) coreIdx.add(new int[]{i, j});
                }
            }
            M = coreIdx.size();
            visited = 0;
            dfs(0, 0, 0);
            bw.append(minLength + "\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }

    public static void dfs(int depth, int connection, int length){
        // 코어가 가장자리에 있는 지 확인
        if (Objects.equals(depth, M)) {
            if (connection > maxConnection) {
                maxConnection = connection;
                minLength = length;
            }
            else if (connection == maxConnection) minLength = Math.min(length, minLength);
            return;
        }

        if(isEdge(coreIdx.get(depth)[0], coreIdx.get(depth)[1])) dfs(depth + 1, connection, length);
        else {
            for (int j = 0; j < 4; j++){
                if (availablePath(coreIdx.get(depth), dr[j], dc[j])){
                    int cnt = markPath(coreIdx.get(depth), dr[j], dc[j]);
                    dfs(depth + 1, connection + 1, length + cnt);
                    removePath(coreIdx.get(depth), dr[j], dc[j]);
                }
            }
            dfs(depth + 1, connection, length);
        }
    }


    public static void removePath(int[] idx, int dr, int dc){
        int nr = idx[0] + dr;
        int nc = idx[1] + dc;
        while (true){
            if (nr == -1 || nr == N || nc == -1 || nc == N) return;
            map[nr][nc] = 0;
            nr += dr;
            nc += dc;
        }
    }
    public static int markPath(int[] idx, int dr, int dc){
        int nr = idx[0] + dr;
        int nc = idx[1] + dc;
        int cnt = 0;
        while (true){
            if (nr == -1 || nr == N || nc == -1 || nc == N) return cnt;
            map[nr][nc] = 2;
            nr += dr;
            nc += dc;
            cnt++;
        }
    }
    public static boolean availablePath(int[] idx, int dr, int dc){
        int nr = idx[0] + dr;
        int nc = idx[1] + dc;

        while (true){
            if (nr == -1 || nr == N || nc == -1 || nc == N) return true;
            if (map[nr][nc] != 0) return false;
            nr += dr;
            nc += dc;
        }
    }

    public static boolean isEdge(int r, int c){
        if (r == 0 || r == N - 1 || c == 0 || c == N - 1) return true;
        return false;
    }
}
