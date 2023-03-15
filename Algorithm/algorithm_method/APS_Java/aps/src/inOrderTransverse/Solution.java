package inOrderTransverse;

import java.io.*;
public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static char[] arr;
    static int N;
    public static void main(String[] args) throws IOException {

        int tc;
        for (tc = 1; tc < 11; tc++){
            bw.append("#").append(String.valueOf(tc)).append(" ");
            N = Integer.parseInt(br.readLine());
            arr = new char[N + 1];

            for (int i = 1; i <= N ; i++)
                arr[i] =  br.readLine().split(" ")[1].charAt(0);
            dfs(1);
            bw.write("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
    public static void dfs(int depth) throws IOException {

        if (depth > N) return;
        dfs(depth * 2);
        bw.write(arr[depth]);
        dfs(depth * 2 + 1);
    }
}