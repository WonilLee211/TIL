package hash;

import java.io.*;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution {

    /** 두 집합에 속하는 문자열 원소의 개수를 출력하는 프로그램
     *
     *
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int T, N, M;

    public static void main(String[] args) throws IOException {
            T = Integer.parseInt(br.readLine());

            for(int tc = 1; tc <= T; tc++){
                int ans = 0;

                st = new StringTokenizer(br.readLine());
                N = Integer.parseInt(st.nextToken());
                M = Integer.parseInt(st.nextToken());

                HashSet<String> first = new HashSet<>();
                st = new StringTokenizer(br.readLine());
                for(int i = 0; i < N; i++){
                    first.add(st.nextToken());
                }
                st = new StringTokenizer(br.readLine());
                for(int i = 0; i < M; i++){
                    if(first.contains(st.nextToken())) ans++;
                }
                bw.append("#").append(String.valueOf(tc)).append(" ").append(String.valueOf(ans)).append("\n");
            }
            bw.flush();
            br.close();
            bw.close();
    }
}
