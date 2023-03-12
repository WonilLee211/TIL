package LongestCommonSequence;

import java.io.*;

public class Solution {

    static int[][] dp;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int T;
    public static void main(String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++){
            String[] arr = br.readLine().split(" ");
            String wordA = arr[0];
            String wordB = arr[1];
            bw.append("#").append(String.valueOf(tc)).append(" ");
            // i 까지 봤을 때 두 문자열에서 최대 공통 길이
            // j  까지 봤을 때 두 문자열에서 최대 공통 길이
            dp = new int[wordA.length() + 1][wordB.length() + 1];

            for (int i = 0; i < wordA.length(); i++){
                for (int j = 0; j < wordB.length(); j++){
                    if (wordA.charAt(i) == wordB.charAt(j))
                        dp[i + 1][j + 1] = dp[i][j] + 1;
                    else // 두 문자가 다를 때, 현재 위치에서 근처 최댓값을 선택하기
                        dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
            bw.append(String.valueOf(dp[wordA.length()][wordB.length()]));
            bw.append("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
