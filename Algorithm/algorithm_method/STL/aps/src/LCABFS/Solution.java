package LCABFS;

import java.io.*;
import java.util.*;

public class Solution {


    static BufferedReader br;

    static {
        try {
            br = new BufferedReader(new FileReader("C:\\\\Users\\\\multicampus\\\\Desktop\\\\LWI\\\\TIL\\\\Algorithm\\\\algorithm_method\\\\STL\\\\aps\\\\src\\\\input.txt"));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    //    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int T, tc, N;
    static long cnt; // 답이 int 범위를 벗어나는 케이스가 있어서 long으로 할당해줘야 한다...
    static int[][] dp;
    static int[] depth, visited;
    static List<List<Integer>> children;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (tc = 1; tc <= T; tc++){
            bw.append("#").append(String.valueOf(tc)).append(" ");
            N = Integer.parseInt(br.readLine());
            dp = new int[100001][20];
            depth = new int[100001];
            visited = new int[100001];
            children = new ArrayList<>();

            for (int i = 0; i < 100001; i++){
                visited[i] = 0;
                children.add(new ArrayList<>());
            }

            st = new StringTokenizer(br.readLine());
            dp[1][0] = 0;
            depth[1] = 0;
            for (int i = 2; i <= N; i++){
                int parent = Integer.parseInt(st.nextToken());
                children.get(parent).add(i);
                dp[i][0] = parent;
                depth[i] = depth[parent] + 1;
            }

            for (int y = 1; y < 20; y++){
                for (int x = 1; x <= N; x++)
                    dp[x][y] = dp[dp[x][y - 1]][y - 1];
            }
            cnt = 0;
            bfs();
            bw.append(String.valueOf(cnt));
            bw.append("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }

    public static void bfs(){
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = 1;
        int pre = 1;
        int cur;

        while (!q.isEmpty()){
            int x = q.poll();
            for (int i = 0; i < children.get(x).size(); i++){
                int y = children.get(x).get(i);
                if (Objects.equals(visited[y], 1)) continue;
                q.add(y);
                visited[y] = 1;
                cur = y;
                LCA(pre, cur);
                pre = cur;
            }
        }
    }

    public static void LCA(int x, int y){

        if(depth[x] > depth[y]){
            int temp;
            temp = x;
            x = y;
            y= temp;
        }
        if (dp[y][0] == x){
            cnt += 1;
            return;
        }

        for (int i = 19; i >= 0; i--){
            if (depth[y] - depth[x] >= (1 << i)){
                y = dp[y][i];
                cnt  += (1 << i);
            }
        }
        if (dp[y][0] != dp[x][0]) {
            for (int i = 19; i >= 0; i--){
                if (dp[x][i] != dp[y][i]){
                    cnt += 2 * (1 << i);
                    x = dp[x][i];
                    y = dp[y][i];
                }
            }
        }
        if (dp[x][0] == dp[y][0]){
            cnt += 2;
        }
    }
}