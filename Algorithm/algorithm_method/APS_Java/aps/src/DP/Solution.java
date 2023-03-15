package DP;

import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] dp;
    static int[] volume, value;
    static int N, T, K, ans;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++){
            bw.append("#").append(String.valueOf(tc)).append(" ");
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            dp = new int[N + 1][K + 1];
            volume = new int[101];
            value = new int[101];
            ans = 0;

            for (int i = 1; i <= N; i++){
                st = new StringTokenizer(br.readLine());
                int v = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                volume[i] = v;
                value[i] = c;
            }
            // dp : i 번 물건까지 써서 j 무게 최대 가치
            for (int i = 1; i <= N; i++){
                for (int j = 0; j <= K; j++){
                    dp[i][j] = dp[i - 1][j];
                    if (volume[i] <= j)
                        dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - volume[i]] + value[i]);
                    ans = Math.max(dp[i][j], ans);
                }
            }
            bw.append(String.valueOf(ans));
            bw.append("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
