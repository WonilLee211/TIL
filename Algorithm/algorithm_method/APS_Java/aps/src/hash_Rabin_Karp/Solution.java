package hash_Rabin_Karp;

import java.io.*;
import java.util.StringTokenizer;

/** 문자열 S에서 문자열 B가 몇 번 등장하는지를 찾는 알고리즘
 *  자열 B의 길이를 p, 문자열 S의 길이를 n이라고 할 때, Brute-Force 알고리즘을 사용하면 최악의 경우 O(pn)의 시간 복잡도가 발생
 *  Rabin-Karp 알고리즘은 해시 값을 사용하여 최악의 경우 O(n+p)의 시간 복잡도
 *
 *  Rabin-Karp 알고리즘을 구현
 *  세 가지 지수(EXPONENT1, EXPONENT2, EXPONENT3)와 해시 함수(hash) 사용
 *  문자열 S에서 문자열 B의 해시 값과 같은 값을 가지는 경우, 문자열 B가 문자열 S에서 등장한 것으로 간주하고 등장 횟수를 증가시킵
 *
 */
public class Solution {
    private static final int EXPONENT1 = 2;
    private static final int EXPONENT2 = 3;
    private static final int EXPONENT3 = 5;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int T;
    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++){
            String b = br.readLine();
            String s = br.readLine();

            bw.append("#").append(String.valueOf(tc)).append(" ")
                    .append(String.valueOf(getCount(b, s))).append("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
    private static int getCount(String string, String pattern){
        int ans = 0;

        int stringLength = string.length();
        int patternLength = pattern.length();

        int stringHash1 = 0, patternHash1 = 0;
        int stringHash2 = 0, patternHash2 = 0;
        int stringHash3 = 0, patternHash3 = 0;

        int power1 = 1, power2 = 1, power3 = 1;

        for (int i = 0; i <= stringLength - patternLength; i++){
            if (i == 0){
                for (int j = 0; j < patternLength; j++){
                    stringHash1 += hash(string.charAt(patternLength - 1 - j), power1);
                    patternHash1 += hash(pattern.charAt(patternLength - 1 - j), power1);

                    stringHash2 += hash(string.charAt(patternLength - 1 - j), power2);
                    patternHash2 += hash(pattern.charAt(patternLength - 1 - j), power2);

                    stringHash3 += hash(string.charAt(patternLength - 1 - j), power3);
                    patternHash3 += hash(pattern.charAt(patternLength - 1 - j), power3);

                    if (j == patternLength - 1 ) continue;
                    power1 *= EXPONENT1;
                    power2 *= EXPONENT2;
                    power3 *= EXPONENT3;
                }
            }
            else {
                stringHash1 = EXPONENT1 * (stringHash1 - hash(string.charAt(i - 1), power1))
                        + string.charAt(patternLength - 1 + i);
                stringHash2 = EXPONENT2 * (stringHash2 - hash(string.charAt(i - 1), power2))
                        + string.charAt(patternLength - 1 + i);
                stringHash3 = EXPONENT3 * (stringHash3 - hash(string.charAt(i - 1), power3))
                        + string.charAt(patternLength - 1 + i);
            }
            if (stringHash1 == patternHash1 && stringHash2 == patternHash2 && stringHash3 == patternHash3)
                ans++;
        }
        return ans;
    }
    private static int hash(int value, int power){
        return value * power;
    }
}
